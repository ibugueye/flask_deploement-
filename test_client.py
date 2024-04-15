import pytest
from flask import json
from api import app  # Make sure this import matches the structure of your project

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
    # Assuming 100002 is one of the SK_ID_CURR in your test data, modify as needed
    assert b'100002' in response.data

def test_prediction(client):
    # Modify this payload to match a valid SK_ID_CURR from your CSV file
    data = {'SK_ID_CURR': 100002}  
    response = client.post('/prediction', json=data)
    response_data = json.loads(response.data)
    assert response.status_code == 200
    assert 'prediction' in response_data
    assert 'probability' in response_data
    assert 'decision' in response_data
