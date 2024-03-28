import unittest
import requests

class Testing_Address(unittest.TestCase):
    API_URL='http://127.0.0.1:5000'
    endpoint='{}/employee/address'.format(API_URL)
    
    def test_1_get_all_address(self):
        response=requests.get(Testing_Address.endpoint)
        self.assertEqual(response.status_code,200)
        
    def test_2_get_particular_address(self):
        AddressID=1
        response=requests.get("{}?AddressID={}".format(Testing_Address.endpoint,AddressID))
        self.assertEqual(response.status_code,200)
        
    def test_3_add_address(self):
        data= {
        "Employee_ref_ID": 1,
        "city_id": 1,
        "country_id": 1,
        "state_id": 1,
        "street": "123 near a",
        "zipcode": "21222"
    }
        response=requests.post(Testing_Address.endpoint,json=data)
        self.assertEqual(response.status_code,201)
        
    def test_4_update_address(self):
        AddressID=13
        data=    {
        "Employee_ref_ID": 1,
        "city_id": 1,
        "country_id": 1,
        "state_id": 1,
        "street": "123 near a",
        "zipcode": "21222"
    }
        response=requests.put("{}?AddressID={}".format(Testing_Address.endpoint,AddressID),json=data)
        self.assertEqual(response.status_code,204)
        
    def test_5_delete_salary(self):
        AddressID=11
        response=requests.delete("{}?AddressID={}".format(Testing_Address.endpoint,AddressID))
        self.assertEqual(response.status_code,204)