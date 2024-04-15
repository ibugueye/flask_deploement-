import pytest
from api import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Deploy flask api' in response.data

def test_get_ids(client):
    response = client.get('/get_ids')
    assert response.status_code == 200
    assert b'100002' in response.data  # Assuming 100002 is one of the SK_ID_CURR in your test data

def test_prediction(client):
    data = {'SK_ID_CURR': 100002}  # Assuming this SK_ID_CURR exists in your test data
    response = client.post('/prediction', json=data)
    assert response.status_code == 200
    assert b'prediction' in response.data
    assert b'probability' in response.data
    assert b'decision' in response.data