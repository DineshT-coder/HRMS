import unittest
import requests

class Testing_Employee(unittest.TestCase):
    API_URL='http://127.0.0.1:5000'
    endpoint='{}/employee'.format(API_URL)
    
    def test_1_get_all_employee(self):
        response=requests.get(Testing_Employee.endpoint)
        self.assertEqual(response.status_code,200)
        
    def test_2_get_particular_employee(self):
        EmployeeID=8
        response=requests.get("{}?EmployeeID={}".format(Testing_Employee.endpoint,EmployeeID))
        self.assertEqual(response.status_code,200)
        
    def test_3_add_employee(self):
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
        response=requests.post(Testing_Employee.endpoint,json=data)
        self.assertEqual(response.status_code,201)
    
    def test_4_update_employee(self):
        EmployeeID=8
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
        response=requests.put("{}?EmployeeID={}".format(Testing_Employee.endpoint,EmployeeID),json=data)
        self.assertEqual(response.status_code,204)
          
    def test_5_delete_employee(self):
        EmployeeId=8
        response=requests.delete("{}?EmployeeID={}".format(Testing_Employee.endpoint,EmployeeId))
        self.assertEqual(response.status_code,200)
