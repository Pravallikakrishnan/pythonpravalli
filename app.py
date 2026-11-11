from flask import Flask, send_file
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def home():
    html_file = Path(__file__).resolve().parent / "index.html"
    return send_file(html_file)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
