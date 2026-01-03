## 2️⃣ `embeddings/` — Semantic Search의 핵심 (✅ 필수)

<pre class="overflow-visible! px-0!" data-start="733" data-end="788"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>embeddings/
├─ build_embeddings.py
└─ config.py
</span></span></code></div></div></pre>

### 왜 필요한가

* Embedding은 **검색 품질의 70%**
* 모델/파라미터/배치 전략을 독립적으로 관리해야 함

### 분리 이유

* chunk 실험과 embedding 실험을 분리
* GPU 제약 고려한 설정 관리

| 파일                | 역할                       |
| ------------------- | -------------------------- |
| build_embeddings.py | 문서 → 벡터 변환          |
| config.py           | 모델명, batch size, device |

📌 **JD 매칭**

> “Semantic Search / Embedding 고도화”

👉 **필수**
