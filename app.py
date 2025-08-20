from flask import Flask, current_app

app = Flask(__name__)


@app.route('/')
def index():
    print(current_app.config['DEBUG'])
    return 'index'


# Without a context manager
app_ctx = app.app_context()
app_ctx.push()
print(current_app.config['DEBUG'])
app_ctx.pop()


# With a context manager
with app.app_context():
    print(current_app.config['DEBUG'])


if __name__ == "__main__":
    app.run(debug=True)
