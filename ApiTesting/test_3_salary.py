import unittest
import requests

class Testing_Salary(unittest.TestCase):
    """Class to test salary-related API endpoints."""
    
    API_URL='http://127.0.0.1:5000'
    endpoint='{}/employee/salary'.format(API_URL)
    
    def token_get(self):
        """Helper method to retrieve token from file and set token header."""
        
        with open(r'headersfile\sample.txt', 'r') as f:
            self.token = f.read()
            self.token = {'Authorization': f'Bearer {self.token}'}

    def test_1_get_all_salary(self):
        """Test GET request to retrieve all salaries."""
        
        self.token_get()    
        response=requests.get(Testing_Salary.endpoint,self.token)
        self.assertEqual(response.status_code,200)
        
    def test_2_get_particular_salary(self):
        """Test GET request to retrieve a particular salary."""
        
        self.token_get()
        SalaryID=1
        response=requests.get("{}?SalaryID={}".format(Testing_Salary.endpoint),headers=self.token)
        self.assertEqual(response.status_code,200)
        
    def test_3_add_salary(self):
        """Test POST request to add a new salary."""
        
        self.token_get()
        data=   {
        "Salary": 50000,
        "EmployeeID": 2
        }
        response=requests.post(Testing_Salary.endpoint,json=data,headers=self.token)
        self.assertEqual(response.status_code,201)
        
    def test_4_update_salary(self):
        """Test PUT request to update an existing salary."""

        self.token_get()
        SalaryID=12
        data={
            "Salary": 55000,
            "EmployeeID": 2,
            }
        response=requests.put("{}?SalaryID={}".format(Testing_Salary.endpoint,SalaryID),json=data,headers=self.token)
        self.assertEqual(response.status_code,200)
    
        
    def test_5_delete_salary(self):
        """Test DELETE request to delete an existing salary."""
        
        self.token_get()
        SalaryID=11
        response=requests.delete("{}?SalaryID={}".format(Testing_Salary.endpoint,SalaryID),headers=self.token)
        self.assertEqual(response.status_code,200)