from qa_guru.schema import schemas
from jsonschema import validate


def test_get_single_user(api_request):
    url = "https://reqres.in/api/users/2"
    response = api_request(url)
    body = response.json()
    assert response.status_code == 200
    validate(body, schema=schemas.GET_SINGLE_USER_SCHEMA)


def test_get_single_user_not_found(api_request):
    url = "https://reqres.in/api/users/23"
    response = api_request(url)
    body = response.json()
    assert response.status_code == 404
    validate(body, schema=schemas.GET_SINGLE_USER_NOT_FOUND)


def test_post_create(api_request):
    name = "Bohdan"
    job = "The boss of beginners"

    url = "https://reqres.in/api/users"
    data = {"name": name, "job": job}
    response = api_request(url, method="POST", data=data)
    body = response.json()

    assert response.status_code == 201
    validate(body, schema=schemas.POST_CREATE)


def test_post_register_successful(api_request):
    email = "eve.holt@reqres.in"
    password = "pistol"

    url = "https://reqres.in/api/register"
    data = {"email": email, "password": password}
    response = api_request(url, method='POST', data=data)
    body = response.json()

    assert response.status_code == 200
    validate(body, schema=schemas.POST_REGISTER_SUCCESSFUL)


def test_post_register_unsuccessful(api_request):
    email = "BohdanBogomDan@gmail.com"

    url = "https://reqres.in/api/register"
    data = {"email": email}
    response = api_request(url, method='POST', data=data)
    body = response.json()

    assert response.status_code == 400
    validate(body, schema=schemas.POST_REGISTER_UNSUCCESSFUL)


def test_put_update(api_request):
    name = "Bohdan Obruch"
    job = "A three-month slave owner"

    url = "https://reqres.in/api/users/2"
    data = {"name": name, "job": job}
    response = api_request(url, method='PUT', data=data)
    body = response.json()

    assert response.status_code == 200
    validate(body, schema=schemas.PUT_UPDATE)


def test_patch_update(api_request):
    name = "Bohdan Obruch"
    job = "sometimes a three and a half month slave owner"

    url = "https://reqres.in/api/users/2"
    data = {"name": name, "job": job}
    response = api_request(url, method='PATCH', data=data)
    body = response.json()

    assert response.status_code == 200
    validate(body, schema=schemas.PUT_UPDATE)


def test_delite(api_request):
    url = "https://reqres.in/api/users/2"
    response = api_request(url, method="DELETE")

    assert response.status_code == 204
