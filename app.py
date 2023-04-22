from flask import Flask, render_template, request, jsonify
from caesar_cipher import encrypt_caesar_cipher

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    print("Encrypt route called")
    data = request.get_json()
    text = data.get('text', '')
    shift = data.get('shift', 0)
    encrypted_text = encrypt_caesar_cipher(text, shift)
    return jsonify({"encrypted_text": encrypted_text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
