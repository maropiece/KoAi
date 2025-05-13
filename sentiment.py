from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Example input
product_description = input("Enter product description: ")

# Run analysis
result = sentiment_pipeline(product_description)

# Display result
label = result[0]['label']
score = round(result[0]['score'], 2)
print(f"Sentiment: {label} (Confidence: {score})")
