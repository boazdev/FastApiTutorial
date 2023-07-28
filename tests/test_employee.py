from fastapi.testclient import TestClient
from pydantic import parse_obj_as
from pydantic import TypeAdapter
from schemas.employee_schema import Employee
from main import app
import pytest

class TestEmployee:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Perform setup actions here (e.g., creating resources, setting up connections)
        print("\nSetup: Before each test function")
        self.client = TestClient(app)
        obj={"username": "test_user", "password": "test123"}
        response = self.client.post("/auth/login", data=obj)
        token_data = response.json()
        self.token_header = {"Authorization": "Bearer " + token_data["access_token"]}
        self.emp_validator = TypeAdapter(Employee)
        self.emp_id =""
        #yield

        # Teardown method: Runs after each test function using this fixture
        # Perform teardown actions here (e.g., releasing resources, closing connections)
        """ print("Teardown: After each test function")
        print("post emp id:", self.emp_id) """
    # Test functions using the fixture
    @pytest.fixture()
    def dummy_employee(self,setup):
        new_emp_data = {
                        "first_name": "dummy",
                        "last_name": "dummy",
                        "start_work_year": 2023,
                        "department_id": "8db55833-295f-11ee-b7be-0242ac110002"
                        }
        print("dummy_employee called")
        response = self.client.post("/employee/",json=new_emp_data,headers=self.token_header)
        self.emp_id = response.json()["id"]
        yield
        print("after dummy yield. delete dummy employee:",self.emp_id)
        if(self.emp_id!=None):
            response = self.client.delete(url=f"/employee/{self.emp_id}",headers=self.token_header)
        
    def test_get_all_employees(self):
        response = self.client.get("/employee/",headers=self.token_header)
        print("test all employees:")
        assert response.status_code == 200
        emp_list = response.json()
        assert len(emp_list)>=4
        
        for emp in emp_list:
            self.emp_validator.validate_python(emp)
    
    def test_create_employee(self): # and also delete it
        new_emp_data = {
                        "first_name": "bax",
                        "last_name": "maxin",
                        "start_work_year": 2022,
                        "department_id": "8db55833-295f-11ee-b7be-0242ac110002"
                        }
        
        response = self.client.post("/employee/",json=new_emp_data,headers=self.token_header)
        #print("response error post:",response.json()["detail"])
        assert response.status_code==200
        new_emp_ret = response.json()
        self.emp_id=new_emp_ret["id"]
        print("called test post employee")
        assert new_emp_ret["first_name"]==new_emp_data["first_name"]
        assert new_emp_ret["last_name"]==new_emp_data["last_name"]
        assert new_emp_ret["start_work_year"]==new_emp_data["start_work_year"]
        assert new_emp_ret["department_id"]==new_emp_data["department_id"]
        assert new_emp_ret["id"]
        url = f"/employee/{self.emp_id}"
        """ print("self emp id url:", self.emp_id) """
        response = self.client.delete(url=url,headers=self.token_header)
        assert response.status_code==200
        #assert False

    #@pytest.mark.run(after="test_create_employee")  # Run this test after test_post_employee 
    
    def test_delete_employee(self,dummy_employee):
        url = f"/employee/{self.emp_id}"
        print("test deleted called,emp id:", self.emp_id)
        response = self.client.delete(url=url,headers=self.token_header)
        assert response.status_code==200
        self.emp_id=None
        

    def test_update_employee(self,dummy_employee):
        url = f"/employee/{self.emp_id}"
        print("test update called,emp id:", self.emp_id)
        put_data = {"first_name":"dummy2","last_name":"dummy3","start_work_year":2002}
        response = self.client.put(url=url,json=put_data,headers=self.token_header)
        assert response.status_code==200
        resp_data= response.json()
        assert(resp_data["first_name"]==put_data["first_name"])
        assert(resp_data["last_name"]==put_data["last_name"])
        assert(resp_data["start_work_year"]==put_data["start_work_year"])

    def test_get_employee_by_id(self,dummy_employee):
        url = f"/employee/{self.emp_id}"
        print("test get emp by id called,emp id:", self.emp_id)
        response = self.client.get(url=url,headers=self.token_header)
        assert response.status_code==200
        resp_data= response.json()
        assert(resp_data["first_name"]=="dummy")
        assert(resp_data["last_name"]=="dummy")
        assert(resp_data["start_work_year"]==2023)
        assert(resp_data["department_id"]=="8db55833-295f-11ee-b7be-0242ac110002")