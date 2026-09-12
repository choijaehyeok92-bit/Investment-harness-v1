"""Replay frozen September 6 renderers in an explicit historical source view.

Only a temporary copy is altered. Later raw additions are not fed backwards
into the frozen run. Current pointers are validated by their own dated run.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from .core import ROOT, read

def check():
    from .review_run import DIRECTORY
    snapshot=read(DIRECTORY+'/authority-input.json')
    lock=read('harness/baseline-lock.json')
    reviewed={x['ticker'] for x in read(DIRECTORY+'/model-specs.json')}
    superseded={'registry/companies.json','reviews/latest.json'}|{f'companies/{t}/latest.json' for t in reviewed}
    with tempfile.TemporaryDirectory(prefix='harness-frozen-replay-') as td:
        dest=Path(td)/'repo'
        shutil.copytree(ROOT,dest,ignore=shutil.ignore_patterns('.git','__pycache__','.pytest_cache'))
        for p in (dest/'companies').glob('*/raw-data/*.json'):
            if str(p.relative_to(dest)) not in lock['raw_file_sha256']:p.unlink()
        (dest/'registry/companies.json').write_text(json.dumps(snapshot['registry'],ensure_ascii=False,indent=2)+'\n')
        code="""
import json
from pathlib import Path
from harness.build import outputs as initial
from harness.deep_report import outputs as deep
skip=set(json.loads(Path('skip-replay.json').read_text()))
counts={}
for label,fn in [('initial',initial),('deep',deep)]:
    files,_=fn();checked=0
    for p,content in files.items():
        if p in skip:continue
        assert Path(p).read_text()==content,('FROZEN_NOT_REPRODUCIBLE',p)
        checked+=1
    counts[label]=checked
print(json.dumps(counts))
"""
        (dest/'skip-replay.json').write_text(json.dumps(sorted(superseded)))
        result=subprocess.run([sys.executable,'-c',code],cwd=dest,text=True,capture_output=True,timeout=180)
        if result.returncode:raise AssertionError(result.stderr[-4000:])
        return json.loads(result.stdout)

if __name__=='__main__':print(json.dumps(check()))
