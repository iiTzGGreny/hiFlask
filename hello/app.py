"""
@Create by greny
@Description: Hello_flask
@Date: 2023/11/4 13:41
@Coding_time: 2023/11/4 13:41
@Modify by: greny
@Script:
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user', defaults={'name': 'Programmer'})
@app.route('/user/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name
