from memory.checkpoint import get_conversation_history


def memory_agent(state):

    history = get_conversation_history(
        state["customer_name"]
    )

    state["history"] = history

    state["response"] = history

    return state