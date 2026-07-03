from typing import TypedDict

class CustomerState(TypedDict):
    # Customer details
    customer_name: str

    # User query
    query: str

    # Classified department
    intent: str

    # Retrieved RAG context
    context: str

    # Previous conversation from SQLite
    history: str

    # Human approval
    approval_required: bool
    approval_status: str

    # Final response
    response: str   



