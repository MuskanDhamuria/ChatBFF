from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)
CORS(app)


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

conversation_history = {}


@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "API is running"}), 200

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message")
    session_id = data.get("sessionId", "default")

    if not message:
        return jsonify({"error": "Message is required"}), 400

    if session_id not in conversation_history:
        conversation_history[session_id] = []

    conversation_history[session_id].append({
        "role": "user",
        "parts": [{"text": message}]
    })

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        history = conversation_history[session_id][:-1]

        chat = model.start_chat(history=history)
        response = chat.send_message(message)

        response_text = response.text

    except Exception as e:
        print("Gemini chat failed, fallback:", e)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response_text = model.generate_content(message).text

    conversation_history[session_id].append({
        "role": "model",
        "parts": [{"text": response_text}]
    })

    return jsonify({
        "success": True,
        "response": response_text,
        "sessionId": session_id
    }), 200

@app.route("/api/clear-session", methods=["POST"])
def clear_session():
    data = request.get_json()
    session_id = data.get("sessionId", "default")
    conversation_history.pop(session_id, None)
    return jsonify({"success": True}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)
