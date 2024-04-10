import unittest
import requests

class Testing_Department(unittest.TestCase):
    """Class to test department-related API endpoints."""
    
    API_URL='http://127.0.0.1:5000'
    endpoint='{}/employee/department'.format(API_URL)
    
    def token_get(self):
        """Helper method to retrieve token from file and set token header."""
        
        with open(r'headersfile\sample.txt', 'r') as f:
            self.token = f.read()
            self.token = {'Authorization': f'Bearer {self.token}'}

    def test_1_get_all_department(self):
        """Test GET request to retrieve all departments."""
        
        self.token_get()
        response=requests.get(Testing_Department.endpoint,headers=self.token)
        self.assertEqual(response.status_code,200)
        
    def test_2_get_particular_department(self):
        """Test GET request to retrieve a particular department."""
        
        self.token_get()
        DepartmentID=3
        response=requests.get("{}?DepartmentID={}".format(Testing_Department.endpoint,DepartmentID),headers=self.token)
        self.assertEqual(response.status_code,200)
        
    def test_3_add_department(self):
        """Test POST request to add a new department."""
        
        self.token_get()
        data={
        "DepartmentName": "HR"        
        }
        response=requests.post(Testing_Department.endpoint,json=data,headers=self.token)
        self.assertEqual(response.status_code,201)
        
    def test_4_update_department(self):
        """Test PUT request to update an existing department."""
        
        self.token_get()
        DepartmentID=5
        data={
                "DepartmentName":"Sale"
            }
        response=requests.put("{}?DepartmentID={}".format(Testing_Department.endpoint,DepartmentID),json=data,headers=self.token)
        self.assertEqual(response.status_code,200)
            
    def test_5_delete_department(self):
        """Test DELETE request to delete an existing department."""
        
        self.token_get()
        DepartmentID=7
        response=requests.delete("{}?DepartmentID={}".format(Testing_Department.endpoint,DepartmentID),headers=self.token)
        self.assertEqual(response.status_code,200)