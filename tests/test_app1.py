import flask

import gothonweb

def login(client, username, password):
    return  client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def logout(client):
    return  client.get('/logout', follow_redirects=True)

app = flask.Flask(__name__)

def test_request():
    with app.test_request_context('/?name=Ulf'):
        assert flask.request.path == '/'
        assert flask.request.args['name'] == 'Ulf'