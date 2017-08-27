def test_get_dashboard_route(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert '<title>Dashboard | ox-sprint</title>' in response
