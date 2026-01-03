## 4️⃣ `reranker/` — 검색 품질을 ‘올리는’ 레이어 (✅ 강력 추천)

<pre class="overflow-visible! px-0!" data-start="1480" data-end="1534"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>reranker/
├─ rerank.py
└─ evaluate_reranker.py
</span></span></code></div></div></pre>

### 왜 필요한가

* Vector Search는 recall 위주
* **Precision은 Reranker가 책임**

### 분리 이유 

* 적용 전/후 실험 비교
* Top-K 전략 실험 가능

| 파일                 | 역할               |
| -------------------- | ------------------ |
| rerank.py            | 검색 결과 재정렬   |
| evaluate_reranker.py | reranker 효과 측정 |


📌 **JD 매칭**

> “랭킹 알고리즘 개발 / 검색 고도화”

👉  **없어도 동작은 함** ,

👉 **있으면 합격 확률 급상승**
