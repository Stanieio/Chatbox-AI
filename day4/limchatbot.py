import os
import streamlit as st
from groq import Groq

client = Groq(api_key="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")   # <-- put your real key

st.title("Groq LLM Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask something")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.messages
    )

    assistant_reply = response.choices[0].message.content

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_reply}
    )

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


