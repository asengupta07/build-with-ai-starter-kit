from utils.generate import (
    generate as generate_response,
    analyse_image as analyse_image_response,
)
from PIL import Image


def generate(prompt: str) -> str:
    conspiracy_prompt = f"You are a conspiracy theorist. Respond to the following prompt like a conspiracy theorist, spinning outlandish conspiracy theories in a way that is engaging and interesting: {prompt}"
    return generate_response(conspiracy_prompt)


def analyse_image(image: Image.Image, prompt: str) -> str:
    conspiracy_prompt = f"You are a conspiracy theorist. Analyse the following image and respond to the following prompt like a conspiracy theorist, spinning outlandish conspiracy theories in a way that is engaging and interesting: {prompt}"
    return analyse_image_response(image, conspiracy_prompt)
