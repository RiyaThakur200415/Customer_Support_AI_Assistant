from utils.llm import llm
from rag.retriever import retrieve_context


def billing_agent(state):

    context = retrieve_context(state["query"])

    state["context"] = context

    prompt = f"""
You are a Billing Support Agent.

Context:
{context}

Customer Question:
{state["query"]}
"""

    response = llm.invoke(prompt)

    state["response"] = response.content

    return state