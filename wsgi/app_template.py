# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def sigin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'li999888':
        return render_template('signin-ok.html', username=username)
    else:
        return '<h1>Wrong username or password</h1>'

if __name__ == '__main__':
    app.run()
