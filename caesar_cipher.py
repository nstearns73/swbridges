import os
from flask import Flask, request, jsonify, render_template

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

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = None
    if request.method == 'POST':
        text = request.form.get('text', '')
        shift = int(request.form.get('shift', 0))
        encrypted_text = encrypt_caesar_cipher(text, shift)
    return render_template('index.html', encrypted_text=encrypted_text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
