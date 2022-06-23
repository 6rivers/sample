from flask import Flask

application = Flask(__name__)
app = application


@app.route('/')
def hello():
    return '<p> Hello World! This is Ranga </p>'
