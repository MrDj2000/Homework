import pytest
from datetime import datetime
from text.controllers import presence


@pytest.fixture
def presence_request():
    return {
        'action': 'presence',
        'time': datetime.now().timestamp(),
        'type': 'status',
        'code': 100,
        'user': {
            'account_name': 'MrDj2000',
            'status': 'Yep, I am here!'
        }
    }


@pytest.fixture
def presence_response_data():
    return 'Hello MrDj2000'


@pytest.fixture
def empty_request():
    return {
        'action': 'presence',
        'time': datetime.now().timestamp()
    }


def test_presence_true(
    presence_request,
    presence_response_data
):
    response = presence(presence_request)
    assert response.get('data') == presence_response_data


def test_presence_empty(empty_request):
    response = presence(empty_request)
    assert response.get('code') == 400