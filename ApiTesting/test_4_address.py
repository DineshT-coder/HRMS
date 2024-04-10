import unittest
import requests

class Testing_Address(unittest.TestCase):
    """
        A test case class for testing the address-related functionalities of the API.
    """
    
    API_URL='http://127.0.0.1:5000'
    endpoint='{}/employee/address'.format(API_URL)
    
    def token_get(self):
        """
        Helper method to retrieve the token from a file and set it as the authorization header.
        """
        with open(r'headersfile\sample.txt', 'r') as f:
            self.token = f.read()
            self.token = {'Authorization': f'Bearer {self.token}'}

    def test_1_get_all_address(self):
        """
        Test case to verify the functionality of retrieving all addresses.
        """
        
        self.token_get()
        response=requests.get(Testing_Address.endpoint,headers=self.token)
        self.assertEqual(response.status_code,200)
        
    def test_2_get_particular_address(self):
        """
        Test case to verify the functionality of retrieving a particular address by its ID.
        """
        self.token_get()
        AddressID=1
        response=requests.get("{}?AddressID={}".format(Testing_Address.endpoint,AddressID),headers=self.token)
        self.assertEqual(response.status_code,200)
        
    def test_3_add_address(self):
        """
        Test case to verify the functionality of adding a new address.
        """
        self.token_get()
        data= {
        "Employee_ref_ID": 1,
        "city_id": 1,
        "country_id": 1,
        "state_id": 1,
        "street": "123 near a",
        "zipcode": "21222"
    }
        response=requests.post(Testing_Address.endpoint,json=data,headers=self.token)
        self.assertEqual(response.status_code,201)
        
    def test_4_update_address(self):
        """
        Test case to verify the functionality of updating an existing address.
        """
        self.token_get()
        AddressID=7
        data=    {
        "Employee_ref_ID": 1,
        "city_id": 1,
        "country_id": 1,
        "state_id": 1,
        "street": "123 near a",
        "zipcode": "21222"
    }
        response=requests.put("{}?AddressID={}".format(Testing_Address.endpoint,AddressID),json=data,headers=self.token)
        self.assertEqual(response.status_code,200)
        
    def test_5_delete_address(self):
        """
        Test case to verify the functionality of deleting an existing address.
        """
        self.token_get()
        AddressID=7
        response=requests.delete("{}?AddressID={}".format(Testing_Address.endpoint,AddressID),headers=self.token)
        self.assertEqual(response.status_code,200)