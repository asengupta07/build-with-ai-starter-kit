from utils.generate import (
    generate as generate_response,
    analyse_image as analyse_image_response,
)
from PIL import Image


def generate(prompt: str) -> str:
    pirate_prompt = (
        f"You are a pirate. Respond to the following prompt like a pirate: {prompt}"
    )
    return generate_response(pirate_prompt)


def analyse_image(image: Image.Image, prompt: str) -> str:
    pirate_prompt = f"You are a pirate. Analyse the following image and respond to the following prompt like a pirate: {prompt}"
    return analyse_image_response(image, pirate_prompt)
