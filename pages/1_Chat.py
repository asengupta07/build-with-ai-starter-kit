import streamlit as st
from utils.generate import generate
import time
from typing import Generator

st.set_page_config(
    page_title="AI Assistant - Chat",
    page_icon="💬",
)

st.title("💬 Chat")


def stream_response(prompt: str) -> Generator[str, None, None]:
    response = generate(prompt)
    response = response.replace("\n", "\n\n")
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.1)


if "messages" not in st.session_state:
    st.session_state.messages = []


def clear_chat():
    st.session_state.messages = []


with st.sidebar:
    st.button("Clear Chat", on_click=clear_chat)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = stream_response(prompt)
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
