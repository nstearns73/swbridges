from flask import Flask, request, render_template_string
from caesar_cipher import encrypt_caesar_cipher, main

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def cipher_game():
    message = "Look under the podium!"
    shift = 3
    encrypted_message = encrypt_caesar_cipher(message, shift)
    user_input = ""

    if request.method == 'POST':
        user_input = request.form['user_input']
        if user_input.lower() == message.lower():
            return render_template_string("Congratulations! You've successfully decrypted the message!")

    return render_template_string('''
        <h1>Welcome to the Cipher Game!</h1>
        <p>Solve the following Caesar cipher to reveal the hidden message:</p>
        <p>{{ encrypted_message }}</p>
        <form method="post">
            <input type="text" name="user_input" placeholder="Enter your solution" required>
            <button type="submit">Submit</button>
        </form>
        {% if user_input %}
            <p>Incorrect! Try again.</p>
        {% endif %}
    ''', encrypted_message=encrypted_message, user_input=user_input)

if __name__ == '__main__':
    app.run()
