import os
import urllib.parse
import werkzeug.urls

if not hasattr(werkzeug.urls, "url_quote"):
    werkzeug.urls.url_quote = urllib.parse.quote

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
