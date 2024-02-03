import pytest
import requests

@pytest.fixture()
def api_request():
    def _make_api_request(url, method="GET", data=None):
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, json=data)
        elif method == "PUT":
            response = requests.put(url, json=data)
        elif method == "PATCH":
            response = requests.patch(url, json=data)
        elif method == "DELETE":
            response = requests.delete(url)
        else:
            raise ValueError("Unsupported HTTP method")
        return response
    return _make_api_request

