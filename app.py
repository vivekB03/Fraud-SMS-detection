from flask import Flask, request, jsonify
import pickle
import traceback
import numpy as np

try:
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    print(" Model and vectorizer loaded successfully")
except Exception as e:
    print(" Error loading model/vectorizer:", e)
    raise

app = Flask(__name__)

@app.route("/")
def home():
    return "SMS Spam Detection API is running!"

@app.route("/test", methods=["GET"])
def test():
    try:
        message = request.args.get("msg")
        if not message:
            return jsonify({"error": "Please provide a message using ?msg=your_text"}), 400

        # Transform input text
        message_vec = vectorizer.transform([message])

        # Predict
        prediction = model.predict(message_vec)[0]

        # Ensure it's a normal Python int
        prediction = int(prediction)

        # Convert numeric output to label
        label = "spam" if prediction == 1 else "Trusted"

        return jsonify({
            "message": message,
            "prediction": label
        })

    except Exception as e:
        print("ERROR in /test:", traceback.format_exc())
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
