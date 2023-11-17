from helper import get_qa_chain, create_vector_db
import streamlit as st

st.title(" Q&A based on previosuly asked FAQS for Ed Tech 🦾")
btn = st.button("Create Knowledgebase")
if btn:
    create_vector_db()

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])