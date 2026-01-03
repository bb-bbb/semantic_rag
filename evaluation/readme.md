## 6️⃣ `evaluation/` — 이 프로젝트의 신뢰성 증명 (✅ 필수)

<pre class="overflow-visible! px-0!" data-start="2193" data-end="2245"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>evaluation/
├─ metrics.py
└─ offline_eval.py
</span></span></code></div></div></pre>

### 왜 필요한가

* “좋아졌다”는 말은 의미 없음
* **지표가 없으면 JD 미충족**

### 분리 이유

* 평가 로직 재사용
* 실험 자동화 가능

| 파일            | 역할          |
| --------------- | ------------- |
| metrics.py      | Recall@k, MRR |
| offline_eval.py | 실험 실행     |

📌 **JD 매칭**

> “성능 평가 방법론 연구 및 개발”

👉 **필수**
