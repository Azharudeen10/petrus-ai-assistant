from llm import get_llm
from rag import get_retriever

llm = get_llm()
retriever = get_retriever()

def is_factual_question(query):
    keywords = [
        "policy", "leave", "rule", "salary",
        "working hours", "benefits", "procedure", "guideline"
    ]
    return any(k in query.lower() for k in keywords)


def agent_answer(query):
    # ---- FACTUAL → RAG ----
    if is_factual_question(query):
        docs = retriever.invoke(query)

        if not docs:
            return "I'm sorry, I couldn't find any relevant information in the documents."

        context = "\n".join([d.page_content for d in docs])

        prompt = f"""
                    You are a company knowledge assistant.
                    Answer strictly from the context below.
                    If the answer is not present, say: "I don't know."

                    Context:
                    {context}

                    Question:
                    {query}
            """

        response = llm.invoke(prompt)   
        return response.content

    # ---- REASONING → LLM ----
    else:
        response = llm.invoke(query)
        return response.content
