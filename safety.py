# safety.py

def calculate_safety_score(sentiment, emotion, ethical_risk):
    score = 100

    # Sentiment impact
    if sentiment == "NEGATIVE":
        score -= 30

    # Emotion impact
    risky_emotions = ["anger", "fear", "disgust", "sadness"]
    if emotion.lower() in risky_emotions:
        score -= 20

    # Ethical risk impact
    if ethical_risk == "High":
        score -= 40
    elif ethical_risk == "Moderate":
        score -= 20
    elif ethical_risk == "Low":
        score -= 10

    # Clamp score between 0 and 100
    score = max(0, min(100, score))

    # Verdict
    if score >= 75:
        verdict = "Safe"
    elif score >= 50:
        verdict = "Safe with parental guidance"
    else:
        verdict = "Unsafe"

    return score, verdict


# Sample test values (replace with real ones later)
if __name__ == "__main__":
    sentiment = "POSITIVE"
    emotion = "joy"
    ethical_risk = "Low"

    score, verdict = calculate_safety_score(sentiment, emotion, ethical_risk)
    print(f"Safety Score: {score}%")
    print(f"Verdict: {verdict}")
