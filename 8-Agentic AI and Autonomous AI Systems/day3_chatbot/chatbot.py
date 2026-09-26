import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

if not api_key:
    st.title("Level1 : Basic Chatbot")
    st.error(
        "Missing API key. Set GOOGLE_API_KEY or GEMINI_API_KEY in your environment or .env file before running this app."
    )
    st.stop()

# create a LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.7,
    google_api_key=api_key,
)

st.title("Level1 : Basic Chatbot")
st.write("Describe your IT problem you are facing and AI will assit you to solve it.")

user_input = st.text_input("Describe your IT issue: ")

if st.button("Ask"):
    if not user_input:
        st.warning("Please write your IT problem first for me to help you")
    else:
        prompt = f"""
        you are a helpful IT helpdesk assistant
        you help the user with simple, practical, and concise answer to the IT Problem the user is facing.
        If the issue is not IT related politely apologies and explain that you only help with IT issues
        if the User issue: {user_input} is IT related you guide with resolution.
        """

        try:
            response = llm.invoke(prompt)
            st.subheader("Helpdesk Response: ")
            st.write(response.content)
        except Exception as e:
            st.error(f"error : {e}")
