import os
import requests
from transformers import pipeline

# Load models
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)
# Only allow robot/AI-related products and toys
allowed_keywords = [
    "robot", "ai", "artificial intelligence", "chatbot", "virtual assistant",
    "companion bot", "toy robot", "intelligent", "autonomous", "smart toy",
    "interactive doll", "ai doll", "voice assistant", "educational robot",
    "emotion ai", "emotional intelligence", "ai-powered", "ai-based",
    "learning robot", "social robot", "ai pet"
]
def is_robot_or_ai_product(name, description):
    combined = f"{name.lower()} {description.lower()}"
    return any(keyword in combined for keyword in allowed_keywords)

# Function to fetch product description using Google Custom Search API
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

# Function to analyze the product using sentiment, emotion, and ethical analysis
def analyze_product(product_name, description):
    # Check if the product is related to robots or AI
    if not is_robot_or_ai_product(product_name, description):
        return {
            "error": "Only AI or robot-related products/toys are supported. Please enter a valid robot or AI product."
        }
    # Run sentiment analysis
    sentiment_result = sentiment_pipeline(description)
    sentiment_label = sentiment_result[0]['label']
    sentiment_score = round(sentiment_result[0]['score'], 2)

    # Run emotion analysis (fixed)
    emotion_output = emotion_pipeline(description)
    emotion_label = emotion_output[0][0]['label']
    emotion_score = round(emotion_output[0][0]['score'], 2)

    # Check for ethical risk (using some keywords to assess the product)
    risk_keywords = ['manipulate', 'unsafe', 'aggression', 'surveillance', 'dependency', 'frustration', 'bias', 'control','spy','adictive',]
    ethical_risk = "High" if any(keyword in description.lower() for keyword in risk_keywords) else "Moderate"

    # Adjust safety score based on ethical risk
    if ethical_risk == "High":
        safety_score = (sentiment_score + emotion_score) / 2 - 0.3  # stronger penalty

    else:
        safety_score = round((sentiment_score + emotion_score) / 2, 2)

    # Make sure safety score is between 0% and 100%
    safety_score = max(min(safety_score, 1.0), 0.0)  # Cap safety score between 0 and 1

    # Verdict
    verdict = "Unsafe" if safety_score < 0.6 else "Safe"

    return {
        "sentiment_label": sentiment_label,
        "sentiment_score": sentiment_score,
        "emotion_label": emotion_label,
        "emotion_score": emotion_score,
        "ethical_risk": ethical_risk,
        "safety_score": safety_score * 100,  # Only multiply by 100 when displaying as percentage
        "verdict": verdict,
    }

# Test directly
if __name__ == "__main__":
    product_name = input("Enter product name: ")
    description = fetch_description(product_name)
    print(f"\nFetched description:\n{description}\n")

    results = analyze_product(product_name, description)

    print(f"\nResults for {product_name}:")
    print(f"Sentiment: {results['sentiment_label']} (Confidence: {results['sentiment_score']})")
    print(f"Emotion: {results['emotion_label']} (Confidence: {results['emotion_score']})")
    print(f"Ethical Risk: {results['ethical_risk']}")
    print(f"Safety Score: {results['safety_score']}")
    print(f"Verdict: {results['verdict']}")
