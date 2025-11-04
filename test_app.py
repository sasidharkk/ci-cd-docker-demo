# test_app.py
from app import app

def test_home():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert b"Hello from CI/CD Pipeline!" in resp.data

