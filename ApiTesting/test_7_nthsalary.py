import unittest
import requests
class Testing_NthSalary(unittest.TestCase):
    """
    A test case class for testing the functionality related to retrieving the Nth highest salary of an employee.
    """
    
    API_URL='http://127.0.0.1:5000'
    endpoint='{}/employee/nthSalary'.format(API_URL)   
    
    def token_get(self):
        """
        Helper method to retrieve the token from a file and set it as the authorization header.
        """

        with open(r'headersfile\sample.txt', 'r') as f:
            self.token = f.read()
            self.token = {'Authorization': f'Bearer {self.token}'}     
    def test_1_GetnthSalary(self):
        """
        Test case to verify the functionality of retrieving the Nth highest salary of an employee.
        """
        
        self.token_get()
        Rank=3
        response=requests.get("{}?Rank={}".format(Testing_NthSalary.endpoint,Rank),self.token)
        self.assertEqual(response.status_code,200)