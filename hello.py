from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Página de inicio</h1>'

@app.route('/hello')
def hello():
    return '<h1>Hola Mundo</h1>'