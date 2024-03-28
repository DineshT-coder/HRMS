import unittest
import requests

class Testing_Qualification(unittest.TestCase):
    API_URL='http://127.0.0.1:5000'
    endpoint='{}/employee/qualification'.format(API_URL)
    
    def test_1_get_all_qualification(self):
        response=requests.get(Testing_Qualification.endpoint)
        self.assertEqual(response.status_code,200)
        
    def test_2_get_particular_qualification(self):
        QualificationID=1
        response=requests.get("{}?QualificationID={}".format(Testing_Qualification.endpoint,QualificationID))
        self.assertEqual(response.status_code,200)
        
    def test_3_add_qualification(self):
        data={
        "Degree": "xyz degree",
        "EmployeeID": 1,
        "GraduationYear": 2016,
        "Institute": "xyz University"
    }
        response=requests.post(Testing_Qualification.endpoint,json=data)
        self.assertEqual(response.status_code,201)
        
    def test_4_update_qualification(self):
        QualificationID=17
        data={
        "Degree": "xyz degree",
        "EmployeeID": 1,
        "GraduationYear": 2016,
        "Institute": "xyz University"
    }
        response=requests.put("{}?QualificationID={}".format(Testing_Qualification.endpoint,QualificationID),json=data)
        self.assertEqual(response.status_code,204)
        
        
    def test_5_delete_qualification(self):
        QualificationID=14
        response=requests.delete("{}?QualificationID={}".format(Testing_Qualification.endpoint,QualificationID))
        self.assertEqual(response.status_code,204)