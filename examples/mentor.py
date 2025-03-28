from utils.generate import generate as generate_response
from utils.generate import analyse_image as analyse_image_response
from utils.parse import parse_json
from tools.mentor import get_job_listings
from PIL import Image

def get_intent(prompt: str) -> dict:
    """
    Determines if the prompt is related to career guidance, job search, or other topics.
    """
    prompt = f"""You are an AI assistant specializing in providing advice related to careers, job opportunities, and job searches. Analyze the following prompt to determine the user's intent: "{prompt}"

    Return your analysis in JSON format with two fields:
    - "intent": Must be one of "career_guidance", "job_search", or "other"
    - "query": If intent is "job_search", extract the key search terms (e.g., job title, location, or industry). Otherwise, use null.

    Examples:
    "What skills should I learn to become a data scientist?" ->
    {{
        "intent": "career_guidance",
        "query": null
    }}

    "Can you help me find marketing jobs in Los Angeles?" ->
    {{
        "intent": "job_search",
        "query": "marketing, Los Angeles"
    }}

    "What’s the weather like today?" ->
    {{
        "intent": "other",
        "query": null
    }}

    "How do I prepare for a software engineering interview?" ->
    {{
        "intent": "career_guidance",
        "query": null
    }}

    "Find me remote graphic design jobs." ->
    {{
        "intent": "job_search",
        "query": "remote, graphic design"
    }}

    "Tell me a joke." ->
    {{
        "intent": "other",
        "query": null
    }}

    Respond only with valid JSON. 
    IMPORTANT: There should be NO text or backticks before or after the JSON."""

    response = generate_response(prompt)
    return parse_json(response)

def generate(prompt: str) -> str:
    """
    Handles career-related queries and generates appropriate responses.
    """
    intent = get_intent(prompt)

    if intent["intent"] == "career_guidance":
        prompt = f"""You are an AI career mentor providing expert career guidance.
        The user asks: "{prompt}"
        Provide a well-structured and concise response in the following JSON format:
        {{
            "advice": "Your response here"
        }}
        Respond only with valid JSON. There should be no text or backticks before or after the JSON."""

        response = generate_response(prompt)
        return parse_json(response)["advice"]

    elif intent["intent"] == "job_search":
        jobs = get_job_listings(intent["query"])

        prompt = f"""You are a job search assistant. The user is looking for jobs matching "{intent['query']}".
        The job listings found: "{jobs}"
        Provide a response in the given JSON format:
        {{
            "job_suggestions": "Your response here"
        }}
        Respond only with valid JSON. There should be no text or backticks before or after the JSON."""

        response = generate_response(prompt)
        return parse_json(response)["job_suggestions"]

    else:
        return generate_response(prompt)

def get_image_intent(image: Image.Image) -> dict:
    """
    Determines whether the uploaded image is a resume or something else.
    """
    prompt = """You are an AI assistant that identifies the type of an uploaded image.
    Determine whether the image is a 'resume' or 'other'.
    
    Return your response in JSON format:
    {
        "intent": "resume" or "other"
    }

    Respond only with valid JSON. There should be no text or backticks before or after the JSON."""

    response = analyse_image_response(image, prompt)
    return parse_json(response)

def get_text_intent(prompt: str) -> dict:
    """
    Determines whether the prompt is related to image analysis, a casual greeting, or something else.
    """
    prompt = f"""You are an AI assistant analyzing user intent.
    Determine if the following prompt is related to 'image_analysis', 'greeting', or 'other'.

    User prompt: "{prompt}"

    Return the result in JSON format:
    {{
        "intent": "image_analysis" or "greeting" or "other"
    }}

    Respond only with valid JSON. There should be no text or backticks before or after the JSON."""

    response = generate_response(prompt)
    return parse_json(response)

def analyse_image(image: Image.Image, prompt: str) -> str:
    """
    Analyzes an image based on the given prompt, but also handles greetings and unrelated messages properly.
    """
    text_intent = get_text_intent(prompt)

    if text_intent["intent"] == "greeting":
        return "Hello! How can I assist you today?"

    elif text_intent["intent"] == "other":
        return "I can analyze resumes. Please upload a resume for review."

    else:  # If it's related to image analysis
        image_intent = get_image_intent(image)

        if image_intent["intent"] == "resume":
            resume_prompt = f"You are an AI resume expert. Analyze the following resume image and provide feedback on any improvements, refinements, or upgrades needed. If the resume is well-structured with no major issues, respond with 'It is all good'. Resume feedback should focus on formatting, clarity, relevant skills, and industry standards.\n\nPrompt: {prompt}"
            return analyse_image_response(image, resume_prompt)
        
        else:
            return "Unsupported image type. Please upload a resume for analysis."
