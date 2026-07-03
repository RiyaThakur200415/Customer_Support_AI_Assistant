def human_approval(state):
    """
    Checks whether the request requires human approval.
    """

    query = state["query"].lower()

    approval_keywords = [
        "refund",
        "cancel",
        "cancellation",
        "account closure",
        "close account",
        "compensation",
        "management"
    ]

    # Check if approval is required
    if any(keyword in query for keyword in approval_keywords):

        state["approval_required"] = True

        print("\n========== HUMAN APPROVAL ==========")
        print("Customer Query:")
        print(state["query"])

        decision = input("\nApprove this request? (yes/no): ").strip().lower()

        if decision == "yes":
            state["approval_status"] = "Approved"
        else:
            state["approval_status"] = "Rejected"
            state["response"] = (
                "Your request has been rejected by the human supervisor."
            )

    else:
        state["approval_required"] = False
        state["approval_status"] = "Not Required"

    return state