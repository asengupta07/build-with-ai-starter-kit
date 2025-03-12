import streamlit as st
from utils.generate import analyse_image
import time
from typing import Generator
from PIL import Image
import io

st.set_page_config(
    page_title="AI Assistant - Image Analysis",
    page_icon="🖼️",
)

st.title("🖼️ Image Analysis")


def stream_response(prompt: str, image: Image.Image) -> Generator[str, None, None]:
    response = analyse_image(image, prompt)
    response = response.replace("\n", "\n\n")
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.1)


if "image_messages" not in st.session_state:
    st.session_state.image_messages = []



def clear_chat():
    st.session_state.image_messages = []


with st.sidebar:
    st.button("Clear Chat", on_click=clear_chat)
    st.subheader("Upload Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    current_image = None

    if uploaded_file is not None:
        image_bytes = uploaded_file.read()
        current_image = Image.open(io.BytesIO(image_bytes))
        st.image(current_image, caption="Uploaded Image", use_column_width="auto")


for message in st.session_state.image_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if current_image is not None:
    if prompt := st.chat_input("What is up?"):
        st.session_state.image_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            stream = stream_response(prompt, current_image)
            response = st.write_stream(stream)
        st.session_state.image_messages.append(
            {"role": "assistant", "content": response}
        )

else:
    st.write("No image uploaded")
