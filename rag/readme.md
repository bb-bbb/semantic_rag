## 5️⃣ `rag/` — 검색을 “답변”으로 바꾸는 계층 (✅ 필수)

<pre class="overflow-visible! px-0!" data-start="1866" data-end="1913"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>rag/
├─ prompt.py
└─ generate_answer.py
</span></span></code></div></div></pre>

### 왜 필요한가

* 검색과 생성은 완전히 다른 책임
* Hallucination 방지의 핵심 영역

### 분리 이유

* 프롬프트 실험 관리
* LLM 교체 쉬움

| 파일               | 역할                 |
| ------------------ | -------------------- |
| prompt.py          | 시스템/유저 프롬프트 |
| generate_answer.py | 검색 결과 → 답변    |

📌 **JD 매칭**

> “RAG 시스템 설계 및 최적화”

👉 **필수**
