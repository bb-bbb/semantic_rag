## 1️⃣ `data/` — 모든 실험의 출발점 (✅ 필수)

<pre class="overflow-visible! px-0!" data-start="319" data-end="366"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>data</span><span>/
├─ raw/
├─ processed/
└─ queries/
</span></span></code></div></div></pre>

### 왜 필요한가

* **원본 데이터와 가공 데이터를 명확히 분리**
* 실험 재현성 확보
* 데이터 정제/전처리 실험 가능

### 하위 디렉토리 의미

| 폴더       | 역할               | 없으면?                   |
| ---------- | ------------------ | ------------------------- |
| raw/       | 수집한 원본 문서   | 원본 손실, 실험 신뢰도 ↓ |
| processed/ | chunked 문서       | chunk 전략 비교 불가      |
| queries/   | 평가용 쿼리 + 정답 | Recall/MRR 계산 불가      |

📌 **JD 매칭 포인트**

> “대용량 데이터 정제 및 분석 경험”

👉 **절대 삭제 ❌**
