import unittest
import requests
class Testing_NthSalary(unittest.TestCase):
    API_URL='http://127.0.0.1:5000'
    endpoint='{}/employee/nthSalary'.format(API_URL)        
    def test_1_GetnthSalary(self):
        Rank=1
        response=requests.get("{}?Rank={}".format(Testing_NthSalary.endpoint,Rank))
        self.assertEqual(response.status_code,200)