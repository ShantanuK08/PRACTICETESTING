import requests
import pytest
import json

class TestAPIS:
    def test_01_listusers(self):
        print("Entry")
        assert True  # Include an assertion to mark the test as valid
        
        header = {}
        body = {}

        url="https://reqres.in/api/users?page=2"
        response = requests.get(url)
        response_json = response.json()
        print()
        assert response.status_code == 200
        assert response_json["data"] is not None, "Response does not contain 'data' key"
        assert response.json()['page'] == 2
        print("Exit")