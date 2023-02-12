from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is data returned from python-flask Web Server!'
