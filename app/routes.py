from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "John"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Edinburgh!'
         },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was cool!'
        }
    ]
    return render_template('index.html', title = "Home", user = user, posts=posts)
