import unittest
import requests

class Testing_Project(unittest.TestCase):
    """
        A test case class for testing the project-related functionalities of the API
    """
    API_URL='http://127.0.0.1:5000'
    endpoint='{}/employee/project'.format(API_URL)
    
    def token_get(self):
        """
        Helper method to retrieve the token from a file and set it as the authorization header.
        """
        with open(r'headersfile\sample.txt', 'r') as f:
            self.token = f.read()
            self.token = {'Authorization': f'Bearer {self.token}'}

    def test_1_get_all_project(self):
        """
        Test case to verify the functionality of retrieving all projects.
        """

        self.token_get()
        response=requests.get(Testing_Project.endpoint,headers=self.token)
        self.assertEqual(response.status_code,200)
        
    def test_2_get_particular_project(self):
        """
        Test case to verify the functionality of retrieving a particular project by its ID.
        """
        self.token_get()
        ProjectID=1
        response=requests.get("{}?ProjectID={}".format(Testing_Project.endpoint,ProjectID),headers=self.token)
        self.assertEqual(response.status_code,200)
        
    def test_3_add_project(self):
        """
        Test case to verify the functionality of adding a new project.
        """
        
        self.token_get()
        data={
                    "Budget": 30000,
                    "DepartmentID": 101,
                    "EmployeeID": 1,
                    "EndDate": "2022-05-25",
                    "ProjectName": "xyzfgrgrgrd",
                    "StartDate": "2022-04-20",
                    "Status": "Complete"
                }
        response=requests.post(Testing_Project.endpoint,json=data,headers=self.token)
        self.assertEqual(response.status_code,201)
        
    def test_4_update_project(self):
        """
        Test case to verify the functionality of updating an existing project.
        """
        
        self.token_get()
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
        response=requests.put("{}?ProjectID={}".format(Testing_Project.endpoint,ProjectID),json=data,headers=self.token)
        self.assertEqual(response.status_code,200)
        
    def test_5_delete_project(self):
        """
        Test case to verify the functionality of deleting an existing project.
        """
        ProjectID=11
        response=requests.delete("{}?ProjectID={}".format(Testing_Project.endpoint,ProjectID),headers=self.token)
        self.assertEqual(response.status_code,200)