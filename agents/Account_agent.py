from utils.llm import llm
from rag.retriever import retrieve_context


def account_agent(state):
    """
    Handles account-related queries such as:
    - Password reset
    - Profile update
    - Account activation/deactivation
    """

    # Retrieve relevant context
    context = retrieve_context(state["query"])
    state["context"] = context

    prompt = f"""
You are an Account Support Agent.

Use ONLY the information provided below to answer the customer's question.

Context:
{context}

Customer Question:
{state["query"]}

Provide a clear, polite, and professional response.
"""

    response = llm.invoke(prompt)

    state["response"] = response.content

    return state