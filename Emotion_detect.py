from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "AIzaSyBayOIKthXyYvAupFXBfVMl0WgkV3c8F50"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

@app.route("/analyze_emotion", methods=["POST"])
def analyze_emotion():
    try:
        data = request.json
        user_input = data.get("text", "").strip()

        if not user_input:
            return jsonify({"error": "請輸入文字"}), 400

        prompt_text = (
            "1.請你推測並回答目前這段文字當中的情緒，例如:生氣、傷心、難過...等等"
            "2.我不需要你的任何解釋，我只要答案而已"
            "3.請用1,2,3,4...來回答我的問題，並最少給我2到3個答案"
            f"文字內容: {user_input}"
        )

        request_body = {
            "contents": [{
                "parts": [{"text": prompt_text}]
            }]
        }

        headers = {"Content-Type": "application/json"}
        response = requests.post(GEMINI_API_URL, json=request_body, headers=headers)
        response_data = response.json()

        if "candidates" in response_data and response_data["candidates"]:
            ai_response = response_data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            ai_response = "無法解析情緒，請重試。"

        return jsonify({"emotion": ai_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8887, debug=True)
