import os
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'

import pytest
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from my DevOps project" in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_visits_increments(client):
    first = client.get('/visits')
    assert first.status_code == 200
    assert first.get_json()['total_visits'] == 1

    second = client.get('/visits')
    assert second.get_json()['total_visits'] == 2
