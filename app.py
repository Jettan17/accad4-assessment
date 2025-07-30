from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "hello worldworlddwomdwo!"

if __name__ == "__main__":
    app.run(port=os.environ.get('PORT', 5000), host="0.0.0.0", debug=True)