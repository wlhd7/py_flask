from flask import Flask, url_for, request
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_from()


def do_the_login():
    return 'do the login from'


def show_the_login_from():
    return 'show the login from'


@app.get('/register')
def register_get():
    return show_the_register_from()


@app.post('/register')
def register_post():
    return do_the_register()


def show_the_register_from():
    return 'show the register from'


def do_the_register():
    return 'fo the register'


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
