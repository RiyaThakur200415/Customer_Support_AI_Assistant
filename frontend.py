import streamlit as st
from graph.workflow import build_graph
from langchain_core.messages import HumanMessage

# Build LangGraph workflow
workflow = build_graph()


def run_frontend():

    st.set_page_config(
        page_title="AI Customer Support",
        page_icon="🤖",
        layout="wide"
    )

    # =========================
    # Header
    # =========================

    st.title("🤖 AI-Powered Customer Support Automation System")
    st.caption("ABC Technologies Customer Support")

    st.markdown(
        "Ask any customer support query related to **Sales, Billing, Technical Support, or Account Management.**"
    )

    st.divider()

    # =========================
    # Main Layout
    # =========================

    left_margin, main, right_margin = st.columns([0.05, 0.90, 0.05])

    with main:

        input_col, info_col = st.columns([2.4, 1])

        # =========================
        # Customer Information
        # =========================

        with input_col:

            with st.container(border=True):

                st.subheader("👤 Customer Information")

                customer_name = st.text_input(
                    "Customer Name",
                    placeholder="Enter your name"
                )

                query = st.text_area(
                    "Customer Query",
                    height=180,
                    placeholder="Describe your issue in detail..."
                )

                submit = st.button(
                    "Submit Query",
                    use_container_width=True
                )

        # =========================
        # Sample Queries
        # =========================

        with info_col:

            with st.container(border=True):

                st.subheader("📌 Sample Queries")

                st.markdown("""
- 💰 What pricing plans do you offer?
- 🔑 I forgot my password.
- 💻 The application crashes when I login.
- 💳 I want a refund.
- 📧 Change my registered email.
- 🧠 What was my previous issue?
                """)

    # =========================
    # Process Request
    # =========================

    if submit:

        if customer_name.strip() == "" or query.strip() == "":
            st.warning("Please enter customer name and query.")
            return

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

        with st.status("Processing Request...", expanded=True) as status:

            st.write("🔍 Detecting customer intent...")
            st.write("📚 Retrieving relevant knowledge...")
            st.write("💾 Loading previous conversation...")
            st.write("🤖 Generating AI response...")

            result = workflow.invoke(state)

            status.update(
                label="Request Completed",
                state="complete"
            )

        st.success("Request Processed Successfully")

        st.divider()

        response_left, response_main, response_right = st.columns([0.05, 0.90, 0.05])

        with response_main:

            # =========================
            # AI Response
            # =========================

            with st.container(border=True):

                st.subheader("🤖 AI Response")

                st.info(result["response"])

            st.markdown("")

            metric1, metric2, metric3 = st.columns(3)

            metric1.metric(
                "🎯 Department",
                result["intent"].title()
            )

            metric2.metric(
                "🛡️ Approval",
                "Yes" if result["approval_required"] else "No"
            )

            metric3.metric(
                "✅ Status",
                result["approval_status"]
            )

            st.markdown("")

            # =========================
            # RAG Context
            # =========================

            with st.expander("📚 Retrieved RAG Context"):

                if result["context"]:
                    st.write(result["context"])
                else:
                    st.write("No relevant documents retrieved.")

            # =========================
            # Conversation History
            # =========================

            with st.expander("📝 Conversation History"):

                if result["history"]:
                    st.write(result["history"])
                else:
                    st.write("No previous conversation found.")

    # =========================
    # Footer
    # =========================

    st.divider()

    st.caption(
        "Powered by LangGraph • FAISS • Google Gemini • SQLite • Streamlit"
    )


if __name__ == "__main__":
    run_frontend()                           