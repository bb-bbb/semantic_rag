import os
from anthropic import Anthropic

client = Anthropic(
    
    api_key=os.getenv('ANTHROPIC_API_KEY')
)


MODEL_NAME = 'claude-3-haiku-20240307'
    
def generate_answer(query: str, context:str) -> str:
    """
    query + context를 받아 Claude로 답변 생성
    """

    prompt = f"""
You are an AI assistant that answers questions using ONLY the provided context.

Rules:
- Use ONLY the information from the context
- If the answer is not in the context, say "I don't know"
- Be concise and factual

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=500,
        temperature=0.0,  # hallucination 최소화
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.content[0].text.strip()

if __name__ == '__main__':
    dummy_context = """
[Document 1 | Source: wikipedia | DocID: ai_washing | Chunk: 1]
AI washing is a deceptive marketing practice involving overstating the use of AI.
"""
    answer = generate_answer(
        query = 'What is AI washing?',
        context= dummy_context
        
    )
    
    print(answer)
    