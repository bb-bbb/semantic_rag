# 📚 Semantic Search + RAG 기반 AI 검색 시스템(wikipedia-인공지능)

## 1. 프로젝트 개요 (Why)

본 프로젝트는 **대용량 문서를 대상으로 한 Semantic Search + RAG(Retrieval-Augmented Generation) 기반 AI 검색 시스템**을 구현하는 것을 목표로 합니다.

단순 키워드 검색이 아닌,

* 문서의 **의미 기반 검색**
* 검색 결과의 **정확도 향상을 위한 reranking**
* 검색된 문서를 근거로 한 **LLM 기반 답변 생성**
* **정량적 평가 지표(Recall@K, MRR)**를 통한 성능 검증

까지 포함한 **엔드투엔드 검색 시스템**을 설계·구현했습니다.

> 본 프로젝트는 연구용 PoC가 아닌,
>
> **실제 서비스 환경을 가정한 구조적 설계와 재현 가능성**에 중점을 둡니다.

### 이번 프로젝트 기준

* 카테고리: **Artificial intelligence**
* 언어: **English Wikipedia** (JD 친화)
* 목표 문서 수: **100~500개**
  * 너 PC 성능에서도 충분히 처리 가능

---

## 2. 전체 시스템 구조

<pre class="overflow-visible! px-0!" data-start="616" data-end="796"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>User</span><span></span><span>Query</span><span>
   ↓
</span><span>Embedding</span><span></span><span>(</span><span>Query</span><span>)</span><span>
   ↓
</span><span>Vector</span><span></span><span>Search</span><span></span><span>(</span><span>FAISS</span><span>)</span><span>
   ↓
</span><span>Top</span><span>-</span><span>K</span><span> 문서 검색
   ↓
</span><span>Reranker</span><span></span><span>(</span><span>Cross</span><span>-</span><span>Encoder</span><span>)</span><span>
   ↓
</span><span>Relevant</span><span></span><span>Context</span><span></span><span>Selection</span><span>
   ↓
</span><span>LLM</span><span></span><span>(</span><span>RAG</span><span>)</span><span>
   ↓
</span><span>Final</span><span></span><span>Answer</span><span>
</span></span></code></div></div></pre>

---

## 3. 디렉토리 구조 및 설계 의도 (Structure)

<pre class="overflow-visible! px-0!" data-start="838" data-end="1613"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>semantic</span><span>-search-rag</span><span>/
│
├─ </span><span>data</span><span>/
│   ├─ raw/              </span><span># 원본 문서 (Wikipedia, PDF, Text 등)</span><span>
│   ├─ processed/        </span><span># Chunk 단위로 전처리된 문서</span><span>
│   └─ queries/          </span><span># 평가용 쿼리 + 정답 문서</span><span>
│
├─ embeddings/           </span><span># 문서 임베딩 생성</span><span>
│   ├─ build_embeddings.py
│   └─ config.py
│
├─ vector_store/         </span><span># 벡터 인덱스 생성 및 로딩</span><span>
│   ├─ build_index.py
│   └─ load_index.py
│
├─ reranker/             </span><span># 검색 결과 재정렬</span><span>
│   ├─ rerank.py
│   └─ evaluate_reranker.py
│
├─ rag/                  </span><span># RAG 기반 답변 생성</span><span>
│   ├─ prompt.py
│   └─ generate_answer.py
│
├─ evaluation/           </span><span># 성능 평가</span><span>
│   ├─ metrics.py        </span><span># Recall@K, MRR</span><span>
│   └─ offline_eval.py
│
├─ api/                  </span><span># FastAPI 기반 서빙</span><span>
│   └─ main.py
│
├─ experiments/          </span><span># 실험 기록</span><span>
│   └─ chunk_strategy.md
│
├─ README.md
└─ requirements.txt
</span></span></code></div></div></pre>

### 설계 핵심 원칙

* **책임 분리 (Separation of Concerns)**
* 실험 단위 교체 가능 (Embedding / Chunk / Reranker)
* 오프라인 평가 → 온라인 서빙까지 확장 가능

---

## 4. 데이터 처리 전략

* [X] 4.1 Raw → Processed

* 대용량 문서를 일정 길이로 **chunking**
* chunk overlap 실험 가능
* 문서 ID, chunk ID 유지

### 4.2 평가 데이터

* 실제 검색 시나리오를 가정한 쿼리
* 쿼리-정답 문서 매핑을 통한 정량 평가

---

## 5. 검색 및 RAG 전략

### 5.1 Semantic Search

* Sentence Transformer 기반 임베딩
* FAISS를 활용한 대규모 벡터 검색

### 5.2 Reranking

* Top-K 문서를 대상으로 Cross-Encoder reranking
* Recall 중심 → Precision 개선

### 5.3 RAG

* 검색된 문서를 **근거(Context)**로 사용
* Hallucination 최소화
* Prompt 분리 설계로 실험 용이성 확보

---

## 6. 평가 방법 (Evaluation)

본 프로젝트는 **정량적 지표 기반 평가**를 필수로 포함합니다.

* **Recall@K** : 정답 문서를 검색 결과에 포함했는지
* **MRR (Mean Reciprocal Rank)** : 정답 문서의 평균 순위

이를 통해:

* Chunk 전략 비교
* Reranker 적용 전/후 비교
* Embedding 모델 비교

가 가능합니다.

---

## 7. 실험 기록 (Experiments)

`experiments/` 디렉토리에는

* Chunk 크기
* Overlap
* 검색 성능 변화

등 **의사결정 과정과 실험 결과를 문서로 기록**합니다.

> 단순 구현이 아닌,
>
> **왜 이 선택을 했는지 설명 가능한 프로젝트**를 목표로 합니다.

---

## 8. 한계 및 개선 방향 (Limitations)

* 대규모 실시간 트래픽에 대한 부하 테스트 미포함
* RAG 응답 품질에 대한 human evaluation 미구현
* 멀티모달 문서(이미지, 표) 처리 미지원

향후:

* Hybrid Search (BM25 + Vector)
* Query Expansion
* Online Feedback 기반 개선

을 고려할 수 있습니다.

---

## 9. 실행 방법

<pre class="overflow-visible! px-0!" data-start="2841" data-end="2884"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install -r requirements.txt
</span></span></code></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="2886" data-end="3077"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(--spacing(9)+var(--header-height))] @w-xl/main:top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span># 임베딩 생성</span><span>
python embeddings/build_embeddings.py

</span><span># 벡터 인덱스 생성</span><span>
python vector_store/build_index.py

</span><span># 오프라인 평가</span><span>
python evaluation/offline_eval.py

</span><span># API 실행</span><span>
uvicorn api.main:app --reload</span></span></code></div></div></pre>
