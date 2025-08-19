from flask import Flask, request

app = Flask(__name__)

with app.app_context():
    with app.test_request_context("/?name=Alice"):
        print(request.args)
    with app.test_request_context("/?name=Bob"):
        print(request.args)
