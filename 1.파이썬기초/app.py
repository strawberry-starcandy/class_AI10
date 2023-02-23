# flask : framework 프로그램
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello World!!</h1>'