from langgraph.graph import StateGraph, END

from graph.Assistant_state import CustomerState

# Nodes
from nodes.classifier import classify_intent, router
from nodes.human_approval import human_approval

# Agents
from agents.Sales_agent import sales_agent
from agents.Technical_agent import technical_agent
from agents.Billing_agent import billing_agent
from agents.Account_agent import account_agent
from agents.Memory_agent import memory_agent
from agents.supervisor_agent import supervisor_agent


def build_graph():

    builder = StateGraph(CustomerState)

    # -------------------------
    # Add Nodes
    # -------------------------

    builder.add_node("Classifier", classify_intent)
    builder.add_node("Sales", sales_agent)
    builder.add_node("Technical", technical_agent)
    builder.add_node("Billing", billing_agent)
    builder.add_node("Account", account_agent)
    builder.add_node("Memory", memory_agent)
    builder.add_node("HumanApproval", human_approval)
    builder.add_node("Supervisor", supervisor_agent)

    # -------------------------
    # Entry Point
    # -------------------------

    builder.set_entry_point("Classifier")

    # -------------------------
    # Conditional Routing
    # -------------------------

    builder.add_conditional_edges(
        "Classifier",
        router,
        {
            "sales": "Sales",
            "technical": "Technical",
            "billing": "Billing",
            "account": "Account",
            "memory": "Memory",
        }
    )

    # -------------------------
    # Normal Flow
    # -------------------------

    builder.add_edge("Sales", "Supervisor")
    builder.add_edge("Technical", "Supervisor")
    builder.add_edge("Account", "Supervisor")
    builder.add_edge("Memory", "Supervisor")

    # -------------------------
    # Billing Flow
    # -------------------------

    builder.add_edge("Billing", "HumanApproval")
    builder.add_edge("HumanApproval", "Supervisor")

    # -------------------------
    # End
    # -------------------------

    builder.add_edge("Supervisor", END)

    return builder.compile()
