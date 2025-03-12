from utils.generate import (
    generate as generate_response,
    analyse_image as analyse_image_response,
)
from PIL import Image


def generate(prompt: str) -> str:
    poet_prompt = (
        f"You are a poet. Respond to the following prompt in a poem, with proper rhyming and structure: {prompt}"
    )
    return generate_response(poet_prompt)


def analyse_image(image: Image.Image, prompt: str) -> str:
    poet_prompt = f"You are a poet. Analyse the following image and respond to the prompt in a poem, with proper rhyming and structure: {prompt}"
    return analyse_image_response(image, poet_prompt)
