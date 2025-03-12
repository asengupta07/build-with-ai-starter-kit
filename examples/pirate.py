from utils.generate import generate as generate_response

def generate(prompt: str) -> str:
    pirate_prompt = f"You are a pirate. Respond to the following prompt like a pirate: {prompt}"
    return generate_response(pirate_prompt)


if __name__ == "__main__":
    print(generate("Hello, how are you?"))
