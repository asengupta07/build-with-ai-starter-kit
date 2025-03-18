import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
import os
import time  # ✅ Add this line for the typing effect

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate(prompt: str) -> str:
    # Simulate a "typing..." effect
    with st.spinner("🤖 Thinking..."):
        time.sleep(2)  # Add delay for realism
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
    
    return response.text  # ✅ Keep your original response handling

def analyse_image(image: Image.Image, prompt: str) -> str:
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content([prompt, image])
    return response.text
