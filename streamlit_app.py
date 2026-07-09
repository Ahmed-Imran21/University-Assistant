# ============================================================
# streamlit_app.py
# Part 1
# ============================================================

import streamlit as st
import sys
from pathlib import Path

# ------------------------------------------------------------
# Allow importing from code_pipeline
# ------------------------------------------------------------

CURRENT_DIR = Path(__file__).resolve().parent

CODE_DIR = CURRENT_DIR / "code_pipeline"

sys.path.append(str(CODE_DIR))

# ------------------------------------------------------------
# Import LangGraph
# ------------------------------------------------------------

from graph import graph

# ------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="University Assistant",
    page_icon="🎓",
    layout="wide",
)

# ------------------------------------------------------------
# Title
# ------------------------------------------------------------

st.title("🎓 University Assistant")

st.markdown(
    """
Welcome!

I'm your AI-powered University Assistant.

Ask me anything about:

- 📅 Academic Calendar
- 📚 Grading Policy
- 📝 Attendance Policy
- 🧪 Laboratory Guidelines
- 🏠 Hostel Rules
- ☎ Contact Directory

I can also remember information about you!
"""
)

# ------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------

with st.sidebar:

    st.header("⚙ Assistant")

    show_sources = st.checkbox(
        "Show Sources",
        value=True,
    )

    show_chunks = st.checkbox(
        "Show Retrieved Chunks",
        value=False,
    )

    st.divider()

    st.header("📄 Available Documents")

    st.markdown("""
- academic_calendar.md
- attendance_policy.md
- grading_policy.md
- hostel_rules.md
- lab_guidelines.md
- contact_directory.md
""")

    st.divider()

    st.header("🧠 Memory")

    if st.button("Show Saved Memory"):

        from memory import get_all_memory

        memory = get_all_memory()

        if len(memory["memories"]) == 0:

            st.info("No memory stored.")

        else:

            for item in memory["memories"]:

                st.write("•", item)

# ============================================================
# PART 2
# Chat Interface
# ============================================================

# ------------------------------------------------------------
# Conversation History
# ------------------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []

# ------------------------------------------------------------
# Display Previous Messages
# ------------------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ------------------------------------------------------------
# User Input
# ------------------------------------------------------------

question = st.chat_input(
    "Ask a question..."
)

# ------------------------------------------------------------
# Process User Question
# ------------------------------------------------------------

if question:

    # -------------------------
    # Show User Message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # -------------------------
    # Run LangGraph
    # -------------------------

    state = {

        "question": question,

        "intent": "",

        "selected_documents": [],

        "retrieved_documents": [],

        "answer": "",

        "needs_human_review": False

    }

    result = graph.invoke(state)

    answer = result["answer"]

    # -------------------------
    # Save Assistant Message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # -------------------------
    # Display Assistant Reply
    # -------------------------

    with st.chat_message("assistant"):

        st.markdown(answer)

# ============================================================
# PART 3
# Human Review Interface
# ============================================================

# ------------------------------------------------------------
# Human Review
# ------------------------------------------------------------

if (
    question
    and result["needs_human_review"]
):

    st.warning("⚠ This response requires human approval.")

    st.subheader("Draft Answer")

    st.write(answer)

    col1, col2 = st.columns(2)

    with col1:

        approve = st.button(
            "✅ Approve"
        )

    with col2:

        reject = st.button(
            "❌ Reject"
        )

    edited_answer = st.text_area(

        "Edit the answer (optional)",

        value=answer,

        height=200,

    )

    save_edit = st.button(
        "💾 Save Edited Answer"
    )

    # ----------------------------------------

    if approve:

        st.success("Answer Approved")

        st.chat_message("assistant").markdown(
            answer
        )

    # ----------------------------------------

    elif reject:

        st.error("Answer Rejected")

    # ----------------------------------------

    elif save_edit:

        st.success("Edited Answer Approved")

        st.chat_message("assistant").markdown(
            edited_answer
        )

# ============================================================
# PART 4
# Nice UI Extras
# ============================================================

# ------------------------------------------------------------
# Developer Mode
# ------------------------------------------------------------

with st.sidebar:

    st.divider()

    developer_mode = st.checkbox(
        "Developer Mode",
        value=False,
    )

# ------------------------------------------------------------
# Show Selected Documents
# ------------------------------------------------------------

if developer_mode and question:

    with st.expander("📄 Selected Documents"):

        docs = result.get(
            "selected_documents",
            [],
        )

        if docs:

            for doc in docs:

                st.write("•", doc)

        else:

            st.write("No documents selected.")

# ------------------------------------------------------------
# Show Retrieved Chunks
# ------------------------------------------------------------

if developer_mode and question and show_chunks:

    with st.expander("📚 Retrieved Chunks"):

        retrieved = result.get(
            "retrieved_documents",
            [],
        )

        if retrieved:

            for i, doc in enumerate(retrieved, start=1):

                st.markdown(f"### Chunk {i}")

                filename = doc.metadata.get(
                    "filename",
                    "Unknown"
                )

                st.write("**Source:**", filename)

                st.code(doc.page_content)

        else:

            st.write("No retrieved chunks.")

# ------------------------------------------------------------
# Show Sources
# ------------------------------------------------------------

if show_sources and question:

    with st.expander("📖 Sources Used"):

        sources = set()

        for doc in result.get(
            "retrieved_documents",
            [],
        ):

            filename = doc.metadata.get(
                "filename",
                "Unknown"
            )

            sources.add(filename)

        if sources:

            for source in sorted(sources):

                st.write("•", source)

        else:

            st.write("No sources available.")

# ------------------------------------------------------------
# Statistics
# ------------------------------------------------------------

with st.sidebar:

    st.divider()

    st.subheader("📊 Statistics")

    st.metric(
        "Messages",
        len(st.session_state.messages)
    )

    if question:

        st.metric(
            "Selected Documents",
            len(result.get(
                "selected_documents",
                []
            ))
        )

        st.metric(
            "Retrieved Chunks",
            len(result.get(
                "retrieved_documents",
                []
            ))
        )

# ------------------------------------------------------------
# Clear Chat
# ------------------------------------------------------------

with st.sidebar:

    st.divider()

    if st.button("🗑 Clear Conversation"):

        st.session_state.messages = []

        st.rerun()