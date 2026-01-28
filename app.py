import streamlit as st
from agent import agent_answer

st.set_page_config(page_title="Petrus AI Assistant", page_icon="🤖")

st.title("🤖 Company AI Assistant")

query = st.text_input("Ask a question: ")

if query:
    with st.spinner("Thinking..."):
        answer = agent_answer(query)
    st.markdown("### Answer:")
    st.write(answer)
