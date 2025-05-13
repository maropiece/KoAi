import os
from flask import Flask, request, jsonify, render_template, send_file
from io import BytesIO
import zipfile
from analyze import analyze_product, fetch_description
import requests


app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/proxy/examples')
def proxy_examples():
    response = requests.get("http://localhost:3000/api/examples")
    return jsonify(response.json())

@app.route("/")
def home():
    return render_template("home.html")  # renamed from home page.html

@app.route("/analyze-page")
def analyze_page():
    return render_template("analysis.html")  # renamed from analysis page.html

@app.route("/example")
def example_page():
    return render_template("example.html")  # renamed from example page.html

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    name = data.get("name", "")
    description = data.get("description", "")

    if not description:
        description = fetch_description(name)
        print("Fetched description:", description)
        

    results = analyze_product(name, description)
    summary_text = f"""
    Product Name: {name}
    Description: {description}
    Sentiment: {results['sentiment_label']} (Confidence: {results['sentiment_score']})
    Emotion: {results['emotion_label']} (Confidence: {results['emotion_score']})
    Ethical Risk: {results['ethical_risk']}
    Safety Score: {results['safety_score']}%
    Verdict: {results['verdict']}
    """

    # Save the summary as a .txt file
    summary_file_path = "summary.txt"
    with open(summary_file_path, "w") as file:
        file.write(summary_text)
    return jsonify(results)
@app.route("/get_summary", methods=["POST"])
def get_summary():
    data = request.get_json()
    name = data.get("name", "")
    description = data.get("description", "")
    if not description:
        description = fetch_description(name)
    results = analyze_product(name, description)
    summary_text = (
        "Analysis Completed! KoAi Wants to Show you the Results:\n\n"
        f"Product Name: {name}\n"
        f"Description: {description}\n"
        f"Emotional Tone: {results['emotion_label']}\n"
        f"Ethical Risk: {results['ethical_risk']}\n"
        f"Safety Score: {results['safety_score']}%\n"
        f"Verdict: {results['verdict']}\n"
        "Thank You for Using KoAi!!"
    )
    with open("summary.txt", "w") as f:
        f.write(summary_text)
    return send_file("summary.txt", as_attachment=False, mimetype='text/plain')

# Route to download the summary as a zip file
@app.route("/download_zip", methods=["POST"])
def download_zip():
    data = request.get_json()
    name = data.get("name", "")
    description = data.get("description", "")
    if not description:
        description = fetch_description(name)
    results = analyze_product(name, description)

    summary_text = (
        "Analysis Completed! KoAi Wants to Show you the Results:\n\n"
        f"Product Name: {name}\n"
        f"Description: {description}\n"
        f"Emotional Tone: {results['emotion_label']}\n"
        f"Ethical Risk: {results['ethical_risk']}\n"
        f"Safety Score: {results['safety_score']}%\n"
        f"Verdict: {results['verdict']}\n"
        "Thank You for Using KoAi!!"
    )
    summary_path = "summary.txt"
    zip_path = "summary.zip"
    with open(summary_path, "w") as f:
        f.write(summary_text)
    with zipfile.ZipFile(zip_path, "w") as zipf:
        zipf.write(summary_path)
    return send_file(zip_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
