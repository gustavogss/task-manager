from app import create_app

def test_integration():
    app = create_app()
    client = app.test_client()
    response = client.get('/api/resource')
    assert response.status_code == 200
