from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request
from flask import url_for, redirect

moje_imie = "Karolina"
msg = "Hello World!"


@app.route("/")
def index():
    output = request.args.get("output")
    if not output:
        output = PLAIN
    return get_formatted(msg, moje_imie, output.lower())


@app.route("/outputs")
def supported_output():
    return ", ".join(SUPPORTED)

@app.route('/ui')
def home():
    return redirect(url_for('firstpage', filename='index2.html'))
