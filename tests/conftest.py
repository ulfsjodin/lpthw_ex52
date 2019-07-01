import pytest
# import os
# import tempfile
import gothonweb
from gothonweb import app


@pytest.fixture
def client():
    # db_fd, gothonweb.app.config['DATABASE'] = tempfile.mkstemp()
    gothonweb.app.config['TESTING'] = True
    client = gothonweb.app.test_client()

    # with gothonweb.app.app_context():
        # gothonweb.init_db()

    yield client

    # os.close(db_fd)
    # os.unlink(gothonweb.app.config['Database']
