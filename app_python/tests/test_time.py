import pytest
import os

from datetime import datetime
from pytz import timezone

from app_python.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_time(client, mocker):
    resp = client.get("/")

    time = datetime.now(timezone('Europe/Moscow')).strftime(os.environ.get('TIME_FORMAT', '%H:%M'))

    html_string = 'Current Moscow time: '.format(time)

    mocker.patch("app_python.app.get_msc_time", return_value=time)

    assert resp.status_code == 200

    assert html_string in str(resp.data)
