import streamlit as st
import requests

st.set_page_config(page_title="Finetuned Model Chat", layout="centered")
st.title("Finetuned Model Chat with FastAPI Backend")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def send_message():
    user_input = st.session_state.user_input
    if user_input.strip():
        url = "http://127.0.0.1:8000/generate/"
        payload = {"query": user_input}
        try:
            response = requests.post(url, json=payload, timeout=60)
            response.raise_for_status()
            bot_reply = response.json().get("response", "")
        except Exception as e:
            bot_reply = f"Error: {e}"
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", bot_reply))
        st.session_state.user_input = ""  
        
chat_container = st.container()
with chat_container:
    for speaker, message in st.session_state.chat_history:
        align = "right" if speaker == "You" else "left"
        color = "#DCF8C6" if speaker == "You" else "#F1F0F0"
        name = "" if speaker == "You" else "🤖 Bot: "
        st.markdown(
            f"<div style='text-align: {align}; background-color: {color}; padding: 8px; border-radius: 10px; margin: 4px 0;'>{name}{message}</div>",
            unsafe_allow_html=True
        )


st.text_input(
    "Type your message...",
    key="user_input",
    on_change=send_message,
    placeholder="Ask anything...",
)