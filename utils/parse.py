import json


def parse_json(response: str) -> dict:
    if response.startswith("```json") or response.startswith("```"):
        response = response[len("```json") or len("```") :]
    if response.endswith("```"):
        response = response[: -len("```")]
    return json.loads(response)
