from flask import Flask
import pytest

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
