from utils.llm import llm
from memory.checkpoint import save_conversation


def supervisor_agent(state):

    prompt = f"""
Improve the following customer response.

Response:
{state["response"]}

Make it professional, polite and concise.
"""

    response = llm.invoke(prompt)

    state["response"] = response.content

    # Save conversation to SQLite
    save_conversation(
    customer_name=state["customer_name"],
    query=state["query"],
    intent=state["intent"],
    response=state["response"]
)

    return state