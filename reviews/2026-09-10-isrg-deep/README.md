# ISRG 2026-09-10 Deep Research Checkpoint

## 목적

Intuitive Surgical (ISRG)을 Investment Harness 원칙에 따라 재평가한 additive-only 심층분석 체크포인트다. 2026-09-06 current authority 이후의 가격, 미국 경쟁구도, FDA recall/field action, Q2 2026 재무·시술·설치기반 증거를 반영한다.

## 결과

- Decision: `WATCH`
- Priority: `P1`
- Buy authorized: `false`
- Business quality: `67/75`
- Total score: `79/100`
- Classification: `Emerging Outlier`
- Price reference: `$353.24` on 2026-09-09
- Required return: `9%`
- Reverse required growth: approximately `12.56%` for years 2-10 under retained base economics
- Bear / Base / Bull: approximately `$124 / $303 / $609` per share
- Open hard vetoes: `moat_shrinkage`, `permanent_loss_probability`

## 중요한 변화

기존 2026-09-06 assessment 대비 moat trajectory를 14/15에서 13/15로 낮췄다. 이유는 현재 해자가 붕괴했다는 증거가 아니라, 2026년 미국에서 Johnson & Johnson OTTAVA, Medtronic Hugo, CMR Versius의 경쟁이 규제 허가/적응증 확대 단계로 현실화되어 미래 해자 확대의 확신도를 낮춰야 하기 때문이다.

FDA의 2026 SureForm Class I recall과 da Vinci 5/SP 관련 Class II field actions도 별도 추적한다. 현 시술·설치기반 성장은 여전히 강하므로 systemic product-quality failure로 판정하지 않는다.

## 저장 파일

- `reviews/2026-09-10-isrg-deep/source-manifest.json`
- `companies/ISRG/analyses/2026-09-10-deep/evidence-ledger.json`
- `companies/ISRG/analyses/2026-09-10-deep/valuation.json`
- `companies/ISRG/analyses/2026-09-10-deep/assessment.json`
- `companies/ISRG/analyses/2026-09-10-deep/thesis.ko.md`
- `reviews/2026-09-10-isrg-deep/README.md`

## Repository safety / authority

이 run은 **current authority promotion이 아니다**.

변경하지 않는 파일/영역:

- `companies/ISRG/latest.json`
- `registry/companies.json`
- `reviews/latest.json`
- `companies/ISRG/raw-data/**`
- `harness/baseline-lock.json`
- deterministic/frozen current-run outputs

`harness/validate.py`는 baseline-lock의 canonical raw file set과 hash, registry/current pointer, deterministic outputs를 엄격히 검증한다. 따라서 새 evidence를 canonical raw-data에 임의 추가하거나 `latest.json`만 변경하지 않는다.

현재 canonical authority는 계속 `companies/ISRG/latest.json`이 가리키는 `2026-09-06-deep`이다. 이번 결과는 main에 병합 가능한 최신 research checkpoint이며, 향후 별도의 reviewed authority run에서 validator-compatible promotion을 수행한다.

## 핵심 다음 조사

1. OTTAVA/Hugo/Versius의 미국 실제 placements, procedure volumes, multi-platform hospital adoption
2. da Vinci 5의 OUS 전환 및 utilization/기구경제성
3. SureForm 및 da Vinci 5/SP recall closure와 adverse-event trend
4. 8개 분기의 lease assets, inventory, PPE, procedure growth, FCF/share bridge
5. 2026 유럽 direct-distribution acquisition의 증분 세후 cash ROIC
6. 자사주 매입가격과 contemporaneous intrinsic value의 discipline

## Harness 경계

높은 의료기기/로봇수술 구조성장성은 company-quality와 valuation evidence를 대체하지 않는다. 저장된 macro/top-down overlay는 risk budget, valuation stress와 연구 우선순위에만 사용하며 ISRG의 100점 score에 직접 가감하지 않는다.
