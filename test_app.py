import pytest
from app import app


@pytest.fixture
def client():
    '''创建测试客户端'''
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c


def test_counter_first_visit(client):
    '''测试首次访问计数器'''
    response = client.get('/counter')

    '''检查状态码'''
    assert response.status_code == 200

    visits_cookie = client.get_cookie('visits')
    first_time_cookie = client.get_cookie('first_time')
    last_time_cookie = client.get_cookie('last_time')

    assert visits_cookie is not None
    assert visits_cookie.value == '1'
    assert last_time_cookie is not None
    assert first_time_cookie is not None


def test_counter_multiple_visit(client):
    '''测试多次访问计数器'''
    response1 = client.get('/counter')
    response2 = client.get('/counter')

    assert 'visits=1; Path=/' in response1.headers.getlist('Set-Cookie')
    assert 'visits=2; Path=/' in response2.headers.getlist('Set-Cookie')


def test_reset_counter(client):
    '''测试重置计数器'''
    client.get('/counter')
    client.get('/counter')

    response = client.get('/reset-counter')

    assert response.status_code == 200

    response_after_reset = client.get('/counter')

    assert response_after_reset.status_code == 200

    visits_cookie = client.get_cookie('visits')

    assert visits_cookie.value == '1'


def test_cookie_expiration_on_reset(client):
    '''测试重置计数器后，cookie过期'''
    client.get('/counter')
    client.get('/reset-counter')

    visits_cookie = client.get_cookie('visits')
    first_time_cookie = client.get_cookie('first_time')
    last_time_cookie = client.get_cookie('last_time')

    assert visits_cookie is None
    assert first_time_cookie is None
    assert last_time_cookie is None
