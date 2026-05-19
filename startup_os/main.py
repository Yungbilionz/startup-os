import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from agents import analyze_startup

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()

        if not data or 'idea' not in data:
            return jsonify({
                "error": "Please provide a startup idea"
            }), 400

        idea = data['idea']

        if len(idea) < 10:
            return jsonify({
                "error": "Please describe your idea in more detail"
            }), 400

        print(f"Analyzing startup idea: {idea}")
        result = analyze_startup(idea)

        return jsonify({
            "success": True,
            "idea": idea,
            "analysis": result
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)