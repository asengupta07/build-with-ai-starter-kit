from utils.generate import generate as generate_response
from utils.parse import parse_json
from tools.news import get_news


def get_intent(prompt: str) -> str:
    prompt = f"""Analyze if the following prompt is requesting news information: "{prompt}"

    Return your analysis in JSON format with two fields:
    - "intent": Must be exactly "news" if requesting news information, or "other" if not
    - "query": If intent is "news", provide the key search terms (1-3 words) to find relevant news. If intent is "other", use null

    Examples:
    "What's happening with Tesla stock?" ->
    {{
        "intent": "news",
        "query": "Tesla stock"
    }}

    "Tell me a joke" ->
    {{
        "intent": "other", 
        "query": null
    }}

    Respond only with valid JSON. 
    IMPORTANT: There should be NO text or backticks before or after the generated JSON."""

    response = generate_response(prompt)

    return parse_json(response)


def generate(prompt: str) -> str:
    intent = get_intent(prompt)

    if intent["intent"] == "news":
        news = get_news(intent["query"])

        prompt = f"""You are a news reporter. You are given a prompt and you need to provide a concise summary of the news.
        The prompt is: "{prompt}"
        The news is: "{news}"
        Provide the response in the given JSON format:
        {{
            "summary": "summary"
        }}
        Respond only with valid JSON. There should be no text or backticks before or after the JSON."""

        response = generate_response(prompt)

        return parse_json(response)["summary"]
    else:
        return generate_response(prompt)
