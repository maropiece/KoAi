import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_description(product_name):
    params = {
        "key": os.getenv("GOOGLE_API_KEY"),
        "cx": os.getenv("GOOGLE_CX"),
        "q": product_name + " product description",
    }
    response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
    data = response.json()

    if "items" in data:
        for item in data["items"]:
            snippet = item.get("snippet", "")
            if len(snippet) > 50 and "summary" not in snippet.lower():
                return snippet
        return data["items"][0].get("snippet", "No description found.")
    else:
        return "No description found."
    