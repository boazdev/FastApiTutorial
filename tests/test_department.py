from fastapi.testclient import TestClient

from pydantic import TypeAdapter
from schemas.department_schema import Department

import pytest

class TestDepartment:
    @pytest.fixture(autouse=True)
    def setup(self,client: TestClient, get_token_header:dict):
        # Perform setup actions here (e.g., creating resources, setting up connections)
        #print("\nSetup: Before each test function")
        self.client = client
        self.token_header = get_token_header
        self.department_validator = TypeAdapter(Department)
        self.department_id =""
        #yield
        # Teardown method: Runs after each test function using this fixture

    @pytest.fixture()
    def dummy_department(self,setup):
        new_department_data = {
                            "name": "Logistics",
                            "manager_id": "4a303b7a-297a-11ee-b7be-0242ac110002",
                            }
        print("dummy_department called")
        response = self.client.post("/department/",json=new_department_data,headers=self.token_header)
        self.department_id = response.json()["id"]
        yield
        print("after dummy yield. delete dummy department:",self.department_id)
        if(self.department_id!=None):
            response = self.client.delete(url=f"/department/{self.department_id}",headers=self.token_header)
        
    def test_get_all_departments(self):
        response = self.client.get("/department/",headers=self.token_header)
        print("test all departments:")
        assert response.status_code == 200
        department_list = response.json()
        assert len(department_list)>=4
        
        for department in department_list:
            self.department_validator.validate_python(department)
    
    def test_create_department(self): # and also delete it
        new_department_data = {
                            "name": "Logistics",
                            "manager_id": "4a303b7a-297a-11ee-b7be-0242ac110002",
                            }
        
        response = self.client.post("/department/",json=new_department_data,headers=self.token_header)
        #print("response error post:",response.json()["detail"])
        assert response.status_code==200
        new_department_ret = response.json()
        
        #print("called test post department")
        assert new_department_ret["name"]==new_department_data["name"]
        assert new_department_ret["manager_id"]==new_department_data["manager_id"]
        assert new_department_ret["id"]
        self.department_id=new_department_ret["id"]
        url = f"/department/{self.department_id}"
        #print("self department id url:", url)
        response = self.client.delete(url=url,headers=self.token_header)
        assert response.status_code==200
 
    def test_delete_department(self,dummy_department):
        url = f"/department/{self.department_id}"
        print("test deleted called,department id:", self.department_id)
        response = self.client.delete(url=url,headers=self.token_header)
        assert response.status_code==200
        self.department_id=None
        

    def test_update_department(self,dummy_department):
        url = f"/department/{self.department_id}"
        print("test update called,department id:", self.department_id)
        put_data = {
                            "name": "Logistics2",
                            "manager_id": "4a303b7a-297a-11ee-b7be-0242ac110002",
                            }
        response = self.client.put(url=url,json=put_data,headers=self.token_header)
        assert response.status_code==200
        resp_data= response.json()
        assert(resp_data["name"]==put_data["name"])
        assert(resp_data["manager_id"]==put_data["manager_id"])

    def test_get_department_by_id(self,dummy_department):
        url = f"/department/{self.department_id}"
        print("test get department by id called,department id:", self.department_id)
        response = self.client.get(url=url,headers=self.token_header)
        assert response.status_code==200
        resp_data= response.json()
        assert(resp_data["name"]=="Logistics")
        assert(resp_data["manager_id"]=="4a303b7a-297a-11ee-b7be-0242ac110002")
        assert(resp_data["id"]==self.department_id)