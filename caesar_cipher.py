def encrypt_caesar_cipher(text, shift):
    encrypted_text = ""

# caesar_cipher.py
from flask import Flask, request, jsonify

app = Flask(__name__)

def encrypt_caesar_cipher(text, shift):
    # ... (the rest of the function code)

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    data = request.get_json()
    text = data.get('text', '')
    shift = data.get('shift', 0)
    encrypted_text = encrypt_caesar_cipher(text, shift)
    return jsonify({"encrypted_text": encrypted_text})

if __name__ == '__main__':
    app.run()
  

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
