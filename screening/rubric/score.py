#!/usr/bin/env python3
"""Outlier Expectation Gap screening calculator.

Usage:
    python score.py inputs.json [inputs2.json ...]

Input: {"ticker": "...", "as_of": "...", "metrics": {"D1M1": 0.42, "D2M4": null, ...},
        "vetoes": {"<veto_id>": "pass"|"investigate"|"confirm"}}

Metrics left out or set to null are treated as unknown: excluded from the domain
denominator and charged the unknown penalty. Nothing is filled in optimistically.
"""
from __future__ import annotations
import json, sys, pathlib

RUBRIC = json.loads((pathlib.Path(__file__).parent/'rubric.json').read_text(encoding='utf-8'))
DOM = {d['id']: d for d in RUBRIC['domains']}
MET = {m['id']: (d, m) for d in RUBRIC['domains'] for m in d['metrics']}
MAXPT = 4


def score_metric(m, v):
    """Return 0..4, or None when the value is unknown."""
    if v is None:
        return None
    if 'bands_special' in m:                      # banded range, e.g. normalization multiple
        for lo, hi, pts in m['bands_special']:
            if (lo is None or v >= lo) and (hi is None or v < hi):
                return pts
        return 0
    inv = m.get('invert', False)
    for edge, pts in m['bands']:
        if edge is None:
            return pts
        if (v <= edge) if inv else (v >= edge):
            return pts
    return 0


def evaluate(inp):
    metrics = inp.get('metrics', {})
    vetoes = inp.get('vetoes', {})
    domains, unknown_total = {}, 0
    for did, d in DOM.items():
        got = mx = 0
        unknown, detail = [], []
        for m in d['metrics']:
            v = metrics.get(m['id'])
            s = score_metric(m, v)
            if s is None:
                unknown.append(m['id']); unknown_total += 1
                detail.append({'id': m['id'], 'name': m['name'], 'value': None, 'points': None})
            else:
                got += s; mx += MAXPT
                detail.append({'id': m['id'], 'name': m['name'], 'value': v, 'points': s})
        n = len(d['metrics'])
        raw = got/mx*100 if mx else None
        disc = 1 - RUBRIC['unknown_penalty']['discount']*len(unknown)/n
        domains[did] = {
            'name': d['name'], 'weight': d['weight'],
            'raw_score': round(raw, 2) if raw is not None else None,
            'score': round(raw*disc, 2) if raw is not None else None,
            'unknown_discount': round(disc, 3),
            'evaluated_metrics': mx//MAXPT, 'metric_count': n,
            'unknown_metrics': unknown, 'detail': detail}

    covered = sum(d['weight'] for d in domains.values() if d['score'] is not None)
    if covered:
        total_raw = sum(d['raw_score']/100*d['weight']
                        for d in domains.values() if d['score'] is not None)/covered*100
        total = sum(d['score']/100*d['weight']
                    for d in domains.values() if d['score'] is not None)/covered*100
        total, total_raw = round(total, 2), round(total_raw, 2)
    else:
        total = total_raw = None

    confirmed = [k for k, v in vetoes.items() if v == 'confirm']
    investigate = [k for k, v in vetoes.items() if v == 'investigate']

    mg = metrics.get('D7M1')          # margin of safety
    asym = metrics.get('D8M1')        # asymmetry ratio
    bull = metrics.get('D8M2')        # bull multiple

    if confirmed:
        screen, why = 'REJECT', f"Hard Veto 확정 {len(confirmed)}건. 점수와 무관하게 REJECT."
    elif covered < 100:
        screen, why = 'INCOMPLETE', f"평가 가중 {covered}/100. 점수를 확정하지 않는다."
    elif bull is not None and bull < 1.0:
        screen, why = 'SCREEN_OUT', 'Bull 가치가 현재가 미만.'
    elif asym is not None and asym < 0.5:
        screen, why = 'SCREEN_OUT', f'비대칭 {asym:.2f} < 0.5.'
    elif total is not None and total < 60 and mg is not None and mg < 0:
        screen, why = 'SCREEN_OUT', '품질과 기대차가 동시에 부족.'
    elif (total is not None and total >= 70 and mg is not None and mg > 0
          and asym is not None and asym >= 1.5):
        screen, why = 'SCREEN_IN', '품질·기대차·비대칭 3요건 충족.'
    else:
        screen, why = 'WATCH', '3요건 중 일부 미충족.'

    if investigate and screen in ('SCREEN_IN', 'WATCH'):
        screen = 'WATCH'
        why += f" 미해소 Hard Veto {len(investigate)}건으로 비중 0% 제한."

    scored = total is not None and covered >= 100
    cls = next((c['label'] for c in RUBRIC['classifications']
                if scored and c['min'] <= total <= c['max']), 'INCOMPLETE')
    pos = next((c['position'] for c in RUBRIC['classifications']
                if scored and c['min'] <= total <= c['max']), 'N/A')
    if confirmed or investigate or screen in ('INCOMPLETE', 'SCREEN_OUT', 'REJECT'):
        pos = '0%'

    return {'ticker': inp.get('ticker'), 'as_of': inp.get('as_of'),
            'total_score': total, 'total_before_discount': total_raw,
            'unknown_metrics': unknown_total,
            'confidence': round(1 - unknown_total/len(MET), 3),
            'coverage_weight': covered, 'classification': cls,
            'screen': screen, 'reason': why, 'position_guide': pos,
            'confirmed_vetoes': confirmed, 'investigate_vetoes': investigate,
            'domains': domains, 'buy_authorized': False}


def main(paths):
    out = []
    for p in paths:
        r = evaluate(json.loads(pathlib.Path(p).read_text(encoding='utf-8')))
        out.append(r)
        print(f"═══ {r['ticker']}  ({r['as_of']})")
        print(f"    총점 {r['total_score']}  (할인 전 {r['total_before_discount']}, "
              f"unknown {r['unknown_metrics']}/{len(MET)}, 신뢰도 {r['confidence']})")
        print(f"    coverage {r['coverage_weight']}/100 · {r['classification']}")
        for did, d in r['domains'].items():
            s = (f"{d['score']:6.1f} (원 {d['raw_score']:.0f} x{d['unknown_discount']})"
                 if d['score'] is not None else "     —")
            u = f"  unknown:{','.join(d['unknown_metrics'])}" if d['unknown_metrics'] else ""
            print(f"      {d['weight']:>3} {d['name']:<22} {s}{u}")
        if r['confirmed_vetoes']:
            print(f"    확정 veto: {r['confirmed_vetoes']}")
        if r['investigate_vetoes']:
            print(f"    미해소 veto: {r['investigate_vetoes']}")
        print(f"    ▶ {r['screen']} — {r['reason']}  비중 {r['position_guide']}\n")
    return out


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    main(sys.argv[1:])
