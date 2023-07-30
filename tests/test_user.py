from fastapi.testclient import TestClient

from pydantic import TypeAdapter
from schemas.user_schema import User
from .conftest import create_user_data 
import pytest

class TestUser:
    @pytest.fixture(autouse=True)
    def setup(self,client: TestClient, get_token_header:dict):
        # Perform setup actions here (e.g., creating resources, setting up connections)
        #print("\nSetup: Before each test function")
        self.client = client
        self.token_header = get_token_header
        self.user_validator = TypeAdapter(User)
        self.user_id =""
        #yield
        # Teardown method: Runs after each test function using this fixture

    @pytest.fixture()
    def dummy_user(self,setup):
        new_user_data = {
                            "username": "dummy_user123",
                            "password": "dummy123",
                            "full_name": "Mr robot",
                            "num_of_actions":10
                            }
        print("dummy_user called")
        response = self.client.post("/user/",json=new_user_data,headers=self.token_header)
        self.user_id = response.json()["id"]
        yield
        print("after dummy yield. delete dummy user:",self.user_id)
        if(self.user_id!=None):
            response = self.client.delete(url=f"/user/{self.user_id}",headers=self.token_header)
        
    def test_get_all_users(self):
        response = self.client.get("/user/",headers=self.token_header)
        print("test all users:")
        assert response.status_code == 200
        user_list = response.json()
        assert len(user_list)>=4
        
        for user in user_list:
            self.user_validator.validate_python(user)
    
    def test_create_user(self): # and also delete it
        new_user_data = create_user_data
        print("test_create_user data: ", new_user_data )
        response = self.client.post("/user/",json=new_user_data,headers=self.token_header)
        #print("response error post:",response.json()["detail"])
        assert response.status_code==200
        new_user_ret = response.json()
        self.user_id=new_user_ret["id"]
        #print("called test post user")
        assert new_user_ret["username"]==new_user_data["username"]
        assert new_user_ret["full_name"]==new_user_data["full_name"]
        assert new_user_ret["num_of_actions"]==new_user_data["num_of_actions"]
        assert new_user_ret["id"]
        url = f"/user/{self.user_id}"
        response = self.client.post("auth/login", data ={"username":new_user_data["username"],
                                                         "password":new_user_data["password"]})
        assert(response.status_code==200)
        #print("self user id url:", url)
        response = self.client.delete(url=url,headers=self.token_header)
        assert response.status_code==200
 
    def test_delete_user(self,dummy_user):
        url = f"/user/{self.user_id}"
        #print("test deleted called,user id:", self.user_id)
        response = self.client.delete(url=url,headers=self.token_header)
        assert response.status_code==200
        self.user_id=None
        

    def test_update_user(self,dummy_user):
        url = f"/user/{self.user_id}"
        #print("test update called,user id:", self.user_id)
        put_data = {"username":"dummy789","full_name":"eric cartman2", "num_of_actions":11}
        response = self.client.put(url=url,json=put_data,headers=self.token_header)
        assert response.status_code==200
        resp_data= response.json()
        #print("update resp data: ", resp_data)
        #assert(resp_data["username"]==put_data["username"])
        assert(resp_data["full_name"]==put_data["full_name"])
        assert(resp_data["num_of_actions"]==put_data["num_of_actions"])

    def test_get_user_by_id(self,dummy_user):
        url = f"/user/{self.user_id}"
        #print("test get user by id called,user id:", self.user_id)
        response = self.client.get(url=url,headers=self.token_header)
        assert response.status_code==200
        resp_data= response.json()
        assert(resp_data["username"]=="dummy_user123")
        assert(resp_data["full_name"]=="Mr robot")
        assert(resp_data["num_of_actions"]==10)
        assert(resp_data["id"]==self.user_id)

    def test_user_actions(self):
       
        new_user_data = create_user_data
        response = self.client.post("/user/",json=new_user_data,headers=self.token_header)
        assert response.status_code==200
        print("test user actions uesr id: ", response.json())
        user_id = response.json()["id"]
        #print("response error post:",response.json()["detail"])
        assert response.status_code==200
        response = self.client.post("auth/login", data ={"username":new_user_data["username"],
                                                   "password":new_user_data["password"]})
        assert response.status_code == 200
        token_data = response.json()
        assert "access_token" in token_data
        assert token_data["access_token"]
        token_header = {"Authorization": "Bearer " + token_data["access_token"]}
        for i in range(new_user_data["num_of_actions"]-1):
            response = self.client.get("/employee/",headers=token_header)
            assert response.status_code==200
        response = self.client.get("/employee/",headers=token_header)
        assert response.status_code!=200
        response = self.client.delete(url=f"/user/{user_id}", headers=self.token_header)
        assert response.status_code == 200
        