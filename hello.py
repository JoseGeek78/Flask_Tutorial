from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return '<h1>Página de inicio</h1>'

@app.route('/hello/<name>')
def hello(name):
    return '<h1>Hola {name}!</h1>'