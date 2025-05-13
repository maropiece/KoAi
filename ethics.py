from transformers import pipeline

# Load the zero-shot classification model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Input from user
description = input("Enter product description: ")

# Custom labels for classification
labels = ["Safe", "Unsafe", "Requires Parental Guidance", "High Ethical Risk", "Low Ethical Risk"]

# Run classification
result = classifier(description, candidate_labels=labels)

# Show results
print("Ethical Risk Classification:")
for label, score in zip(result['labels'], result['scores']):
    print(f"{label}: {round(score * 100, 2)}%")
