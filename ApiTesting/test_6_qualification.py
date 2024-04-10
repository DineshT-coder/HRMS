import unittest
import requests

class Testing_Qualification(unittest.TestCase):
    """
    A test case class for testing the qualification-related functionalities of the API.
    """
    API_URL='http://127.0.0.1:5000'
    endpoint='{}/employee/qualification'.format(API_URL)
    
    def token_get(self):
        """
        Helper method to retrieve the token from a file and set it as the authorization header.
        """
        with open(r'headersfile\sample.txt', 'r') as f:
            self.token = f.read()
            self.token = {'Authorization': f'Bearer {self.token}'}

    def test_1_get_all_qualification(self):
        """
        Test case to verify the functionality of retrieving all qualifications.
        """
        self.token_get()

        response=requests.get(Testing_Qualification.endpoint,headers=self.token)
        self.assertEqual(response.status_code,200)
        
    def test_2_get_particular_qualification(self):
        """
        Test case to verify the functionality of retrieving a particular qualification by its ID.
        """
        self.token_get()
        QualificationID=1
        response=requests.get("{}?QualificationID={}".format(Testing_Qualification.endpoint,QualificationID),headers=self.token)
        self.assertEqual(response.status_code,200)
        
    def test_3_add_qualification(self):
        """
        Test case to verify the functionality of adding a new qualification.
        """
        self.token_get()
        data={
        "Degree": "xyz degree",
        "EmployeeID": 1,
        "GraduationYear": 2016,
        "Institute": "xyz University"
    }
        response=requests.post(Testing_Qualification.endpoint,json=data,headers=self.token)
        self.assertEqual(response.status_code,201)
        
    def test_4_update_qualification(self):
        """
        Test case to verify the functionality of updating an existing qualification.
        """
        self.token_get()
        QualificationID=17
        data={
        "Degree": "xyz degree",
        "EmployeeID": 1,
        "GraduationYear": 2016,
        "Institute": "xyz University"
    }
        response=requests.put("{}?QualificationID={}".format(Testing_Qualification.endpoint,QualificationID),json=data,headers=self.token)
        self.assertEqual(response.status_code,200)
        
        
    def test_5_delete_qualification(self):
        """
        Test case to verify the functionality of deleting an existing qualification.
        """
        self.token_get()
        QualificationID=14
        response=requests.delete("{}?QualificationID={}".format(Testing_Qualification.endpoint,QualificationID),headers=self.token)
        self.assertEqual(response.status_code,200)