from utils.llm import llm
from rag.retriever import retrieve_context


def sales_agent(state):

    context = retrieve_context(state["query"])

    state["context"] = context

    prompt = f"""
You are a Sales Support Agent.

Answer the customer using the information below.

Context:
{context}

Customer Question:
{state["query"]}
"""

    response = llm.invoke(prompt)

    state["response"] = response.content

    return state