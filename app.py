from flask import Flask, request, make_response, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/counter')
def counter():
    visit_count = int(request.cookies.get('visits', 0)) + 1
    time_now = datetime.now().strftime('%y-%m-%d %H:%M:%S')
    first_time = request.cookies.get('first_time', 'this_time')
    if first_time == 'this_time':
        first_time = time_now
    last_time = time_now

    resp = make_response(render_template(
        'counter.html',
        visit_count=visit_count,
        first_time=first_time,
        last_time=last_time))

    resp.set_cookie('visits', str(visit_count))
    resp.set_cookie('first_time', first_time)
    resp.set_cookie('last_time', last_time)

    return resp


@app.route('/reset-counter')
def reset_counter():
    resp = make_response(render_template('reset.html'))
    resp.set_cookie('visits', '', expires=0)
    resp.set_cookie('first_time', '', expires=0)
    resp.set_cookie('last_time', '', expires=0)
    return resp
