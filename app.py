from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>hello world</p>"


@app.route("/<name>")
def hello(name):
    return f"hello {escape(name)}"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'
    return f'Subpath {subpath}'
# /path/<script>alert("injection attack")</script>


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return f'{escape(username)}\'s name'


@app.route('/http-request/<username>')
def http_request(username):
    print(url_for('http_request', username='wlhd'))
    return 'http request'


with app.test_request_context():
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


if __name__ == "__main__":
    app.run(debug=True)
