import unittest
import requests

class Testing_Employee(unittest.TestCase):
    """Class to test employee-related API endpoints."""
    
    API_URL='http://127.0.0.1:5000'
    endpoint='{}/employee'.format(API_URL)
    
    
    def token_get(self):
        """Helper method to retrieve token from file and set token header."""
        
        with open(r'headersfile\sample.txt', 'r') as f:
            self.token = f.read()
            self.token = {'Authorization': f'Bearer {self.token}'}
            
    def test_1_get_all_employee(self):
        """Test GET request to retrieve all employees."""
        
        self.token_get()
        response=requests.get(Testing_Employee.endpoint,headers=self.token)
        self.assertEqual(response.status_code,200)
        
    def test_2_get_particular_employee(self):
        """Test GET request to retrieve a particular employee."""
         
        self.token_get()
        EmployeeID=2
        response=requests.get("{}?EmployeeID={}".format(Testing_Employee.endpoint,EmployeeID),headers=self.token)
        self.assertEqual(response.status_code,200)
        
    def test_3_add_employee(self):
        """Test POST request to add a new employee."""
        
        self.token_get()
        data={
        "DateOfBirth": "2001-05-15",
        "DepartmentID": 2,
        "Email": "sahil@gmail.com",
        "FirstName": "sahil",
        "HireOfDate": "2022-03-13",
        "LastName": "barolia",
        "ManagerID": 2,
        "PhoneNumber": "1212567896",
        "Position": "Account Executive"
        }
        response=requests.post(Testing_Employee.endpoint,json=data,headers=self.token)
        self.assertEqual(response.status_code,201)
    
    
    def test_4_update_employee(self):
        """Test PUT request to update an existing employee."""
        
        self.token_get()
        EmployeeID=7
        data={
        "DateOfBirth": "2001-05-15",
        "DepartmentID": 2,
        "Email": "sahil@gmail.com",
        "FirstName": "sahil",
        "HireOfDate": "2022-03-13",
        "LastName": "barolia",
        "ManagerID": 6,
        "PhoneNumber": "1212567897",
        "Position": "Account Executive"
    }
        response=requests.put("{}?EmployeeID={}".format(Testing_Employee.endpoint,EmployeeID),json=data,headers=self.token)
        self.assertEqual(response.status_code,200)
          
    def test_5_patch_method_employee(self):
        """Test PATCH request to partially update an employee."""

        self.token_get()
        EmployeeID=7
        data={
        "PhoneNumber": "5552567897"
    }
        response=requests.patch("{}?EmployeeID={}".format(Testing_Employee.endpoint,EmployeeID),json=data,headers=self.token)
        self.assertEqual(response.status_code,200)      
    
    def test__delete_employee(self):
        """Test DELETE request to delete an existing employee."""
        
        self.token_get()
        EmployeeId=7
        response=requests.delete("{}?EmployeeID={}".format(Testing_Employee.endpoint,EmployeeId),headers=self.token)
        self.assertEqual(response.status_code,200)
