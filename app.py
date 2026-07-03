from graph.workflow import build_graph
from memory.checkpoint import create_database

# Create SQLite database (only once)
create_database()

# Build the LangGraph workflow
workflow = build_graph()

print("=" * 50)
print(" AI-Powered Customer Support Automation System ")
print("=" * 50)

while True:

    customer_name = input("\nEnter Customer Name: ")

    query = input("Enter Your Query: ")

    state = {
        "customer_name": customer_name,
        "query": query,
        "intent": "",
        "context": "",
        "history": "",
        "approval_required": False,
        "approval_status": "",
        "response": ""
    }

    result = workflow.invoke(state)

    print("\n" + "=" * 50)
    
    print("Final Response")
    print("=" * 50)
    print(result["response"])

    choice = input("\nDo you want to continue? (yes/no): ").lower()

    if choice != "yes":
        print("\nThank you for using the Customer Support System.")
        break