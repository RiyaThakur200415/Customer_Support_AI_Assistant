from utils.llm import llm
from rag.retriever import retrieve_context


def technical_agent(state):

    context = retrieve_context(state["query"])

    state["context"] = context

    prompt = f"""
You are a Technical Support Engineer.

Context:
{context}

Customer Question:
{state["query"]}
"""

    response = llm.invoke(prompt)

    state["response"] = response.content

    return state