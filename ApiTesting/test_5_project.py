import unittest
import requests

class Testing_Project(unittest.TestCase):
    API_URL='http://127.0.0.1:5000'
    endpoint='{}/employee/project'.format(API_URL)
    
    def test_1_get_all_project(self):
        response=requests.get(Testing_Project.endpoint)
        self.assertEqual(response.status_code,200)
        
    def test_2_get_particular_project(self):
        ProjectID=1
        response=requests.get("{}?ProjectID={}".format(Testing_Project.endpoint,ProjectID))
        self.assertEqual(response.status_code,200)
        
    def test_3_add_project(self):
        data={
                    "Budget": 30000,
                    "DepartmentID": 101,
                    "EmployeeID": 1,
                    "EndDate": "2022-05-25",
                    "ProjectName": "xyzfgrgrgrd",
                    "StartDate": "2022-04-20",
                    "Status": "Complete"
                }
        response=requests.post(Testing_Project.endpoint,json=data)
        self.assertEqual(response.status_code,201)
        
    def test_4_update_project(self):
        ProjectID=15
        data=    {
        "Budget": 30000,
        "DepartmentID": 101,
        "EmployeeID": 1,
        "EndDate": "2022-05-25",
        "ProjectName": "xyzfgrgrgrd",
        "StartDate": "2022-04-20",
        "Status": "Complete"
    }
        response=requests.put("{}?ProjectID={}".format(Testing_Project.endpoint,ProjectID),json=data)
        self.assertEqual(response.status_code,204)
        
    def test_5_delete_salary(self):
        ProjectID=11
        response=requests.delete("{}?ProjectID={}".format(Testing_Project.endpoint,ProjectID))
        self.assertEqual(response.status_code,204)