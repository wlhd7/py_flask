from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>hello world</p>"


@app.route("/<name>")
def hello(name):
    return f"hello {escape(name)}"


if __name__ == "__main__":
    app.run(debug=True)
