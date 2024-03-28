import unittest
import requests

class Testing_Department(unittest.TestCase):
    API_URL='http://127.0.0.1:5000'
    endpoint='{}/employee/department'.format(API_URL)
    
    def test_1_get_all_department(self):
        response=requests.get(Testing_Department.endpoint)
        self.assertEqual(response.status_code,200)
        
    def test_2_get_particular_department(self):
        DepartmentID=9
        response=requests.get("{}?DepartmentID={}".format(Testing_Department.endpoint,DepartmentID))
        self.assertEqual(response.status_code,200)
        
    def test_3_add_department(self):
        data={
        "DepartmentName": "HR"        
        }
        response=requests.post(Testing_Department.endpoint,json=data)
        self.assertEqual(response.status_code,201)
        
    def test_4_update_department(self):
        DepartmentID=113
        data={
                "DepartmentName":"Sale"
            }
        response=requests.put("{}?DepartmentID={}".format(Testing_Department.endpoint,DepartmentID),json=data)
        self.assertEqual(response.status_code,204)
            
    def test_5_delete_department(self):
        DepartmentID=113
        response=requests.delete("{}?DepartmentID={}".format(Testing_Department.endpoint,DepartmentID))
        self.assertEqual(response.status_code,204)