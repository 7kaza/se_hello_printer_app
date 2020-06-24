from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for, make_response
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index2.html')

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
