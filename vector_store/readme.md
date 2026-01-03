## 3️⃣ `vector_store/` — 대용량 검색을 가능하게 하는 계층 (✅ 필수)

<pre class="overflow-visible! px-0!" data-start="1137" data-end="1193"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>vector_store/
├─ build_index.py
└─ load_index.py
</span></span></code></div></div></pre>

### 왜 필요한가

* 임베딩 ≠ 검색
* 인덱싱 전략은 독립적인 설계 대상

### 분리 이유

* FAISS ↔ Chroma 교체 가능
* 인덱스 재빌드/로딩 분리

| 파일           | 의미                |
| -------------- | ------------------- |
| build_index.py | 벡터 인덱스 생성    |
| load_index.py  | 검색 시 인덱스 로딩 |

📌 **JD 매칭**

> “대규모 검색 트래픽 고려한 시스템 설계”

👉 **필수**
