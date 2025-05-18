app.py
from flask import Flask, request, jsonify
from generator import generate_text
from flask_cors import CORS

app = Flask(_name_)
CORS(app)  # Enable CORS so frontend can access backend

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')

    if not prompt.strip():
        return jsonify({'response': 'Please enter a valid prompt.'}), 400

    try:
        result = generate_text(prompt)
        return jsonify({'response': result})
    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'}), 500

if _name_ == '_main_':
    app.run(debug=True)