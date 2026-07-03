from utils.llm import llm


def classify_intent(state):

    query = state["query"]

    prompt = f"""
You are an AI Customer Support Classifier.

Classify the customer query into EXACTLY ONE category.

Categories:
- sales
- technical
- billing
- account
- memory

Rules:
- sales → pricing, subscription plans, product information
- technical → crashes, installation, login, errors, configuration
- billing → payment, refund, invoice
- account → password reset, profile update, activation
- memory → previous issue, previous conversation

Return ONLY one word.

Customer Query:
{query}
"""

    try:
        response = llm.invoke(prompt)

        intent = response.content.strip().lower()

        valid = [
            "sales",
            "technical",
            "billing",
            "account",
            "memory"
        ]

        if intent not in valid:
            intent = "technical"

        state["intent"] = intent

    except Exception as e:

        print("Classifier Error:", e)

        # Default route if the LLM fails
        state["intent"] = "technical"

    return state


def router(state):
    return state["intent"]