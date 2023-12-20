from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Página de inicio'

@app.route('/hello')
def hello():
    return 'Hola Mundo'