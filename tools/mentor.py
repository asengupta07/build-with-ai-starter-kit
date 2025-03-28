import requests
import re
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")

def get_job_listings(query: str) -> str:
    query = re.sub(r"\s+", "+", query)

    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    params = {"query": query, "page": "1", "num_pages": "1"}

    response = requests.get(url, headers=headers, params=params)

    job_items = []

    if response.status_code == 200:
        jobs = response.json().get("data", [])

        for job in jobs[:3]:
            title = job.get("job_title", "Unknown Title")
            company = job.get("employer_name", "Unknown Company")
            location = job.get("location", "Unknown Location")
            link = job.get("job_apply_link", "#")

            job_items.append(f"• {title} at {company}, {location}\n  {link}")

    return "\n\n".join(job_items) if job_items else "No jobs found for this query."
