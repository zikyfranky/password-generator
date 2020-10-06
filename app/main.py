from flask import Flask, render_template, request
from app.passwordGenerator import generate

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def getPassword():
    data = request.args.to_dict()
    return generate(data)
