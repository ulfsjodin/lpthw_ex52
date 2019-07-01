import flask
import pytest
from gothonweb.app import app

app.config["TESTING"] = True
client = app.test_client()
web = app.test_client()


@pytest.fixture()
def web_get():
    rv = web.get('/', follow_redirects=True)
    return rv


def test_index(web_get):
    assert web_get.status_code == 200


def test_game():
    rv = web.get('/game', follow_redirects=True)
    assert rv.status_code == 200


def test_no_site():
    rv = web.get('/traktor', follow_redirects=True)
    assert rv.status_code == 404


def test_form(web_get):
    assert b'The Gothons' in web_get.data


def test_data():
    data = "Central"
    rv = web.get("/game", follow_redirects=True, data=data)
    assert b'Central' in rv.data


def test_more():
    data = {'name': 'Ulf', 'greet': 'hello'}
    rv = web.get("/game", follow_redirects=True, data=data)
    assert b'Percal' in rv.data


def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)


def test_request():
    with app.test_request_context('/?name=Ulf'):
        assert flask.request.path == '/'
        assert flask.request.args['name'] == 'Ulf'
