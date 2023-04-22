import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def encrypt_caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift_amount) % 26 + 97)
            else:
                encrypted_text += chr((ord(char) - 65 + shift_amount) % 26 + 65)
        else:
            encrypted_text += char

    return encrypted_text

@app.route('/')
def index():
    return "Welcome to the Caesar cipher API! Use the /encrypt endpoint with a POST request to encrypt text."

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    data = request.get_json()
    text = data.get('text', '')
    shift = data.get('shift', 0)
    encrypted_text = encrypt_caesar_cipher(text, shift)
    return jsonify({"encrypted_text": encrypted_text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
