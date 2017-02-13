# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action='/signin' method='post'>
            <p>Username <input name='username'></p>
            <p>Password <input name='password'></p>
            <p><button type='submit'>Sign In</p>
            </form>'''

@app.route('/signin', methods=['POST'])
def signin_post():
    if request.form['username']=='admin' and request.form['password']=='li999888':
        return '<h1>Hello admin!</h1>'
    else:
        return '<h1>Bad username or password</h1>'

if __name__ == '__main__':
    app.run()

