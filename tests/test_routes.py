from quote_project import app


def test_root_route():
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.data is not None
    assert response.status_code == 200


def test_about_route():
    client = app.test_client()
    url = '/home'

    response = client.get(url)
    assert response.data is not None
    assert response.status_code == 200


def test_about_route():
    client = app.test_client()
    url = '/about'

    response = client.get(url)
    assert response.data is not None
    assert response.status_code == 200


def test_register_route():
    client = app.test_client()
    url = '/register'

    response = client.get(url)
    assert response.data is not None
    assert response.status_code == 200


def test_register_route():
    client = app.test_client()
    url = '/register'

    response = client.get(url)
    assert response.data is not None
    assert response.status_code == 200


def test_login_route():
    client = app.test_client()
    url = '/login'

    response = client.get(url)
    assert response.data is not None
    assert response.status_code == 200


def test_profilemgmt_route():
    client = app.test_client()
    url = '/profilemgmt'

    response = client.get(url)
    assert response.data is not None
    assert response.status_code == 200


def test_fuelquote_route():
    client = app.test_client()
    url = '/fuelquote'

    response = client.get(url)
    assert response.data is not None
    assert response.status_code == 200


def test_history_route():
    client = app.test_client()
    url = '/history'

    response = client.get(url)
    assert response.data is not None
    assert response.status_code == 200