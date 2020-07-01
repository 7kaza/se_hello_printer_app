from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for
from datetime import timedelta
app = Flask(__name__)

app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
    return render_template("index2.html")

@app.route('/<name>')
def hello(name=None):
    return render_template('index2.html', name=name)

@app.route('/admin')
def admin():
    return redirect(url_for('home'))

@app.route('/Karolina')
def error():
   return "Witaj, mamy to samo imie :) "

if __name__ == "__main__":
	app.run(debug=True)
