import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to Flask App demo"

@app.route('/who are you')
def hello():
    return 'I\'m Ramesh Velpula. what about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
