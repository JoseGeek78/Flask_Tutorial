from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello(name, age):
    return f'<h1>Hola, {name}, tu edad es {age}!</h1>'
