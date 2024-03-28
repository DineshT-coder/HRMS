import unittest
import requests

class Testing_Salary(unittest.TestCase):
    API_URL='http://127.0.0.1:5000'
    endpoint='{}/employee/salary'.format(API_URL)
    
    def test_1_get_all_salary(self):
        response=requests.get(Testing_Salary.endpoint)
        self.assertEqual(response.status_code,200)
        # SalaryID=1
        response=requests.get("{}?SalaryID={}".format(Testing_Salary.endpoint))
        self.assertEqual(response.status_code,200)
        
    def test_3_add_salary(self):
        data=   {
        "Salary": 50000,
        "EmployeeID": 2
        }
        response=requests.post(Testing_Salary.endpoint,json=data)
        self.assertEqual(response.status_code,201)
        
    def test_4_update_salary(self):
        SalaryID=12
        data={
            "Salary": 55000,
            "EmployeeID": 2,
            }
        response=requests.put("{}?SalaryID={}".format(Testing_Salary.endpoint,SalaryID),json=data)
        self.assertEqual(response.status_code,204)
    
        
    def test_5_delete_salary(self):
        SalaryID=11
        response=requests.delete("{}?SalaryID={}".format(Testing_Salary.endpoint,SalaryID))
        self.assertEqual(response.status_code,204)