from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def counter():
    # 使用 get() 方法，如果 visits 不存在，不会报错，并给 visits 赋值: 0
    count = int(request.cookies.get('visits', 0)) + 1
    resp = make_response(f'''
        <p>You have visit this site {count} times</p>
        <a href="/reset">Reset Counter</a>
    ''')
    resp.set_cookie('visits', str(count))
    return resp


@app.route('/reset')
def reset():
    resp = make_response('''
        <p>Counter has been reset</p>
        <a href="/">Restart counter</a>
    ''')
    # 将名为 visits 的 cookie 的值设为空支付串，将过期时间设置为过去的时间（立即过期） == 立即删除该 cookie
    resp.set_cookie('visits', '', expires=0)
    return resp
