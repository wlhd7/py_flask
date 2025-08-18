from flask import Flask
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


if __name__ == "__main__":
    app.run(debug=True)
