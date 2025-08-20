from flask import Flask, make_response, render_template

app = Flask(__name__)


@app.route('/')
def index():
    resp = make_response(render_template('index.j2'))
#    resp.set_cookie('username', 'wlhd')
    return resp
