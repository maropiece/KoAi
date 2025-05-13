from transformers import pipeline

# Load emotion recognition pipeline
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

# Example input
product_description = input("Enter product description: ")

# Run analysis
results = emotion_pipeline(product_description)[0]

# Sort and show top emotion
sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)
top_emotion = sorted_results[0]
print(f"Emotion: {top_emotion['label']} (Confidence: {round(top_emotion['score'], 2)})")
