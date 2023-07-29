from fastapi.testclient import TestClient

from pydantic import TypeAdapter
from schemas.shift_schema import Shift

import pytest

class TestShift:
    @pytest.fixture(autouse=True)
    def setup(self,client: TestClient, get_token_header:dict):
        # Perform setup actions here (e.g., creating resources, setting up connections)
        #print("\nSetup: Before each test function")
        self.client = client
        self.token_header = get_token_header
        self.shift_validator = TypeAdapter(Shift)
        self.shift_id =""
        #yield
        # Teardown method: Runs after each test function using this fixture

    @pytest.fixture()
    def dummy_shift(self,setup):
        new_shift_data = {
                            "date_time": "2024-07-25",
                            "starting_hour": 5,
                            "ending_hour": 10
                            }
        print("dummy_shift called")
        response = self.client.post("/shift/",json=new_shift_data,headers=self.token_header)
        self.shift_id = response.json()["id"]
        yield
        print("after dummy yield. delete dummy shift:",self.shift_id)
        if(self.shift_id!=None):
            response = self.client.delete(url=f"/shift/{self.shift_id}",headers=self.token_header)
        
    def test_get_all_shifts(self):
        response = self.client.get("/shift/",headers=self.token_header)
        print("test all shifts:")
        assert response.status_code == 200
        shift_list = response.json()
        assert len(shift_list)>=4
        
        for shift in shift_list:
            self.shift_validator.validate_python(shift)
    
    def test_create_shift(self): # and also delete it
        new_shift_data = {
                            "date_time": "2024-07-25",
                            "starting_hour": 5,
                            "ending_hour": 10
                            }
        
        response = self.client.post("/shift/",json=new_shift_data,headers=self.token_header)
        #print("response error post:",response.json()["detail"])
        assert response.status_code==200
        new_shift_ret = response.json()
        self.shift_id=new_shift_ret["id"]
        #print("called test post shift")
        assert new_shift_ret["date_time"]==new_shift_data["date_time"]
        assert new_shift_ret["starting_hour"]==new_shift_data["starting_hour"]
        assert new_shift_ret["ending_hour"]==new_shift_data["ending_hour"]
        assert new_shift_ret["id"]
        url = f"/shift/{self.shift_id}"
        #print("self shift id url:", url)
        response = self.client.delete(url=url,headers=self.token_header)
        assert response.status_code==200
 
    def test_delete_shift(self,dummy_shift):
        url = f"/shift/{self.shift_id}"
        print("test deleted called,shift id:", self.shift_id)
        response = self.client.delete(url=url,headers=self.token_header)
        assert response.status_code==200
        self.shift_id=None
        

    def test_update_shift(self,dummy_shift):
        url = f"/shift/{self.shift_id}"
        print("test update called,shift id:", self.shift_id)
        put_data = {"date_time": "2024-07-27","starting_hour": 11,"ending_hour": 16}
        response = self.client.put(url=url,json=put_data,headers=self.token_header)
        assert response.status_code==200
        resp_data= response.json()
        assert(resp_data["date_time"]==put_data["date_time"])
        assert(resp_data["starting_hour"]==put_data["starting_hour"])
        assert(resp_data["ending_hour"]==put_data["ending_hour"])

    def test_get_shift_by_id(self,dummy_shift):
        url = f"/shift/{self.shift_id}"
        print("test get shift by id called,shift id:", self.shift_id)
        response = self.client.get(url=url,headers=self.token_header)
        assert response.status_code==200
        resp_data= response.json()
        assert(resp_data["date_time"]=="2024-07-25")
        assert(resp_data["starting_hour"]==5)
        assert(resp_data["ending_hour"]==10)
        assert(resp_data["id"]==self.shift_id)