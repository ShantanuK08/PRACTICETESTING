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

    def test_02_singleusers(self):
        print("inside test case 2")
        assert True

        header = {}
        body = {}

        url = "https://reqres.in/api/users/2"
        response = requests.get(url)
        response_json = response.json()
        
        print( response_json)
        assert response.status_code == 200
        assert response_json["data"]['id']==2
        assert response_json["data"]['email'] 
        assert response_json


        print(json.dumps(response_json, indent=4)) 
        print("User ID:", response_json["data"]["id"])
        print("Email:", response_json["data"]["email"])

        print("exit test case 2")



    def test_03_single_user_not_found(self):
        print ("inside test case 3")

        header ={}
        body = {}

        url = "https://reqres.in/api/users/23"
        response = requests.get(url)
        response_json = response.json
        print(response_json)
        
        assert response.status_code == 404
        
        print("exit test case 3")


    def test_04_list_resourse(self):
        print("inside testcase 4")

        header = {}
        body = {}

        url = "https://reqres.in/api/unknown"
        response = requests.get(url)
        response_json = response.json()
        print(response_json)

        assert response.status_code == 200


        # assert response_json["data"][0]['id'] #Access the first element of the list: response_json["data"][0] accesses the first element of the list (since Python lists are 0-indexed).

        
        # Check if 'data' exists and is a list with at least one item
        if "data" in response_json and isinstance(response_json["data"], list) and len(response_json["data"]) > 0:
             assert "id" in response_json["data"][0]  # Ensure the 'id' exists in the first item
        else:
             print("No data or empty list found.")



        #isinstance(response_json["data"], list): # This checks if the value corresponding to the "data" key is a list.
                                                  # If the value is a list, isinstance() will return True, otherwise it returns False.
                                                  # len(response_json["data"]) > 0:
                                                  # This checks if the list response_json["data"] contains at least one element.
                                                  # The len() function returns the length of the list, and > 0 ensures that the list isn't empty.

        if "email" in response_json["data"][0]:
         assert response_json["data"][0]["email"]
        else:
            print("No email found in the first element.")

        

    # Print User ID and Email
        print("User ID:", response_json["data"][0]["id"])  # Access the first item and then its "id"
        

        print("exit test case 4")



    def test_05_single_resourse(self):
        print ("enter case 5")

        header = {}
        body ={}
        
        url = "https://reqres.in/api/unknown/2"
        response = requests.get(url)
        response_json = response.json()
        print(response_json)

        assert response.status_code == 200

        if "data" in response_json and isinstance(response_json["data"],list) and len(response_json["data"]) > 0:
            assert response_json['data'][0]['id']
            assert response_json["data"][0]["email"]
            
        else:
            print("No data or empty list found.")
            print("No email found in the first element.")


        print("User ID:", response_json["data"]["id"])
        print("Name:", response_json["data"]["name"])
        
        print("exit test case 5")
 

    def test_06_single_resourse_notfound(self):
        print("enter test case 6")
    
        header={}
        body ={}

        url = "https://reqres.in/api/unknown/23"        
        response = requests.get(url)
        response_json = response.json()
        print(response_json)

        assert response.status_code == 404

          # Add if-else to print message based on status code
        if response.status_code == 404:
            print("404 Not Found")
        else:
            print(f"Unexpected status code: {response.status_code}")

        print("exit test case 6")




    def test_07_create(self):
        print("enter test case 7")

        header = {
        "Content-Type": "application/json"
        }

        body = {
        "name": "morpheus",
        "job": "leader"
        }

        url = "https://reqres.in/api/users" 
        response = requests.post(url)
        response_json = response.json()
        print(response_json)

        assert response.status_code == 201

         # Check the response status code & Id & CreatedAt
        if response.status_code == 201:
            print("Status code is 201")
            assert 'id' in response_json  # Ensure the 'id' is in the response 
            assert 'createdAt' in response_json  # Ensure the 'createdAt' field is present
            
        
    # Ensure 'name' is in the response (if it's expected)
        if 'name' in response_json:
            assert response_json['name'] == body['name']  # Ensure the 'name' matches the input data

        else:
            print(f"Unexpected Status Code:{response.status_code}")  #f"...": This syntax indicates that it's a formatted string.
            assert response.status_code == 201  # Fail the test if status code is not 201

        
        # # Check if 'id' is present in the response # FOR UNDERSTANDING

        # if "id" in  response_json:
        #     print("Id is present.:",response_json["id"])
        # else:
        #     print("Id not found")

        # # Check if 'id' is a string

        # if isinstance(response_json.get('id'),str):
        #     print("Id is a String:",response_json['id'])
        # else:
        #     print("Id is not a string")


        print("exit test case 7")
            


    def test_08_update(self):
        print("enter test case 8")

        header = {
        "Content-Type": "application/json"
        }

        body ={
        "name": "morpheus",
        "job": "zion resident"
        }

        url = "https://reqres.in/api/users/2" 
        response = requests.put(url,json=body, headers=header) #The PUT request updates an existing resource, and the server responds with metadata (e.g., updatedAt) confirming the update.
        response_json = response.json()
        print(response_json)

        assert response.status_code == 200

        if  response.status_code == 200:
            print("Update Successful")


        # Check if 'updatedAt' is in the response and assert its presence
            assert 'updatedAt' in response_json  # Ensure 'updatedAt' is present in the response

        # You may not receive 'name' and 'job' in the response based on the API design
        # Instead, check the 'updatedAt' field, as it's likely returned to indicate when the update occurred
            assert response_json['updatedAt'] is not None  # Ensure 'updatedAt' is not None, indicating an update was made



        # If you expect the updated data to be returned, you can also assert for 'name' and 'job' in the response
            assert 'name' in response_json, "'name' field is missing from the response after update."
            assert 'job' in response_json, "'job' field is missing from the response after update."

        # Optionally, you can assert if the values returned match the body you sent, though it might not be part of the API response
            assert response_json['name'] == body['name'], f"Expected 'name' to be {body['name']}, but got {response_json['name']}"
            assert response_json['job'] == body['job'], f"Expected 'job' to be {body['job']}, but got {response_json['job']}"
        else:
            print("Update Unsuccessful")
            print((f"Unexpected Status Code:{response.status_code}"))

        print("exit test case 8")


    def test_09_update2(self):
        print("enter test case 9")

        
        header = {
        "Content-Type": "application/json"
        }


        body = {
        "name": "morpheus",
        "job": "zion resident"
        }
        
        url = "https://reqres.in/api/users/2" 
        response= requests.patch(url,json=body,headers=header)
        response_json = response.json()
        print(response_json)

        assert response.status_code == 200

        
        if  response.status_code == 200:
            print("Update Successful")


        # Check if 'updatedAt' is in the response and assert its presence
            assert 'updatedAt' in response_json  # Ensure 'updatedAt' is present in the response

        # You may not receive 'name' and 'job' in the response based on the API design
        # Instead, check the 'updatedAt' field, as it's likely returned to indicate when the update occurred
            assert response_json['updatedAt'] is not None  # Ensure 'updatedAt' is not None, indicating an update was made



        # If you expect the updated data to be returned, you can also assert for 'name' and 'job' in the response
            assert 'name' in response_json, "'name' field is missing from the response after update."
            assert 'job' in response_json, "'job' field is missing from the response after update."

        # Optionally, you can assert if the values returned match the body you sent, though it might not be part of the API response
            assert response_json['name'] == body['name'], f"Expected 'name' to be {body['name']}, but got {response_json['name']}"
            assert response_json['job'] == body['job'], f"Expected 'job' to be {body['job']}, but got {response_json['job']}"
        else:
            print("Update Unsuccessful")
            print((f"Unexpected Status Code:{response.status_code}"))
        
        print("exit test case 9")


    def test_10_delete(self):
        print("enter test case 10")

        header ={}
        body = {}
 
        url = "https://reqres.in/api/users/2"

        response = requests.delete(url,headers=header, json=body)
    
          # Print status code to check if deletion was successful
        print(response.status_code)  # Expect 204 for successful delete
    

        if response.status_code == 204:
            print("Delete Successful")
        else:
            print(f"Delete Unsuccessful: {response.status_code}")



    # No need to call .json() if the response is empty or contains no JSON
    # Optionally, you can assert that the status code is 204
    

        print("exit testcase 10")



        
        


        