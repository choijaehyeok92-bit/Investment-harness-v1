# NVDA 2026-09-10 심층분석 체크포인트

## 결론

- **WATCH / P1 / buy_authorized=false**
- 사업품질 **64/75**
- 총점 **78/100 — Emerging Outlier**
- 최신 완료 미국장 기준가: **$223.67 (2026-09-09)**
- retained Bear / Base / Bull: **$68.45 / $220.78 / $555.98**
- 9% hurdle reverse growth: **약 9.59% (years 2-10)**
- Open veto: **low_quality_growth / incremental_roic_collapse / moat_shrinkage / permanent_loss_probability**

## 핵심 업데이트

Q2 FY2027 매출은 $96.2B로 106% YoY 증가했고 Data Center는 $89.0B로 117% 증가했다. Q3 가이던스는 중국 Data Center compute 매출을 전혀 가정하지 않고도 $108B다. Vera Rubin은 full-production 램프 단계로 진입했다.

TTM은 FY2026 + H1 FY2027 - H1 FY2026으로 연결했다.

- Revenue: **$302.97B**
- Net income: **$192.88B**
- OCF: **$134.36B**
- NVIDIA-definition FCF: **$126.886B**
- TTM SBC: **$7.241B**
- Conservative FCF-minus-SBC diagnostic: **$119.645B**

사업 현금창출은 강화됐지만 경제적 자본노출도 크게 늘었다.

- Supply/capacity commitments: **$279B**
- H1 publicly-held equity purchases: **$42.404B**
- Gross disclosed guarantees after August SB Energy/OpenAI support: **$108.5B**
- Hugging Face agreed acquisition price: **$12.9303B**
- H1 repurchases: **$39.8B**

또한 H1 operating cash flow 설명에서 회사는 일부 대형 multi-quarter 계약의 결제기간 연장으로 accounts receivable이 증가했다고 밝혔다. 따라서 수요의 질은 출하량만이 아니라 고객의 독립 현금수익률과 receivable behavior로 검증해야 한다.

## 사업 해자

글로벌 full-stack moat는 강화 중이다. CUDA, networking, system architecture, libraries, Blackwell/Rubin cadence와 대규모 cloud deployment가 이를 지지한다.

반면 중국에서는 수출규제가 현지 AI chip과 CUDA-compatible migration path를 키우고 있고, hyperscaler custom chips와 merchant accelerators가 inference 일부 workload를 잠식할 가능성이 커졌다. 따라서 moat는 **global strengthening with localized/workload-specific pressure**로 판정했다.

## 밸류에이션

기존 2026-09-06 deep cash-scenario architecture를 비교 가능성을 위해 유지하고 9월 9일 가격만 동기화했다. Base는 $220.78로 현재가와 사실상 동일하다.

기존 Base의 year-1 revenue $500B, owner-margin path 39%→35%, terminal 22x, 9% required return을 유지하면 현재가가 요구하는 years 2-10 revenue growth는 약 9.59%다. 이는 현실적으로 가능한 범위지만, 10년 duration과 높은 mature owner margin을 요구한다. 따라서 `price_requires_unrealistic_bull_case`는 PASS지만 margin of safety는 부족하다.

## Red Team 핵심

가장 중요한 위험은 단순 GPU 경쟁이 아니다. NVIDIA가 AI boom의 공급자인 동시에 고객/생태계 자본 제공자, 투자자, 보증자로 확대되면서 **수요와 NVIDIA 자본 사이의 부분적 circularity**가 생길 수 있다. 공급약정, 투자지분, 보증, 결제기간 연장, 고객금융은 독립 손실로 이중계산하지 않되 하나의 correlated AI-cycle stress로 봐야 한다.

9월 10일 Reuters가 보도한 Groq 거래 DOJ 조사도 management-integrity veto를 바로 열 근거는 아니지만 자본배분 및 규제 모니터 항목으로 추가했다.

## 행동 조건

가격 하락만으로 증액하지 않는다. 다음이 복수로 확인될 때 STARTER/NORMAL 승격을 검토한다.

1. receivable days와 결제기간 정상화 + Data Center/FCF per share 성장 지속
2. ecosystem investments/guarantees/financing의 realized return이 9% hurdle 상회
3. Rubin 대규모 배치와 system economics 유지
4. custom accelerator 확대에도 NVIDIA workload share/CUDA/networking attach/pricing power 유지
5. 가격 또는 owner cash 개선으로 보수적 Base 대비 명확한 expectation gap 확보

## Repository status

이 실행은 **additive-only deep research checkpoint**다. `companies/NVDA/latest.json`, `registry/companies.json`, `reviews/latest.json`, canonical raw-data, `harness/baseline-lock.json` 및 frozen deterministic outputs는 변경하지 않는다. 현재 canonical authority는 별도 reviewed promotion 전까지 2026-09-06-deep을 유지한다.
