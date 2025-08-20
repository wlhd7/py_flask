from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    print(request.method, request.path)
    return 'index'


# Without a context manager
app_request_ctx = app.test_request_context()
app_request_ctx.push()
print(request.method, request.path)
app_request_ctx.pop()


# With a context manager
with app.test_request_context():
    print(request.method, request.path)


if __name__ == "__main__":
    app.run(debug=True)
