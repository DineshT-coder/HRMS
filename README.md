
# Human Resource Manaeent System using Flask

This Human Resource Management System is a web application built using Flask, a lightweight Python web framework. It allows businesses to manage their employee data efficiently.

# Features
### User Authentication: Secure user authentication system for accessing the application.
### Employee CRUD Operations: Easily add, view, update, and delete employee records.

# Setup

### Installation:

#### `Clone the repository: git clone <repository-url>`
#### `Install dependencies: pip install -r requirements.txt`
## API Reference

### Authentication

### User Registration
#### Endpoint: http://127.0.0.1:5000/user
#### Method: POST
#### Parameters:
    username (string): User's username.
    password (string): User's password.

### User login
#### Endpoint: http://127.0.0.1:5000/login
#### Method: POST
#### Parameters:
    username (string): User's username.
    password (string): User's password.

#### Response
    {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDA3NzA5NSwianRpIjoiMDU3NTViYjYtMDY3YS00M2NlLTg5MTUtNWM4NmMwYTQ3MTliIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNzEwMDc3MDk1LCJjc3JmIjoiZTQwNzk0MmUtMWJmOC00NWExLTg3ZWMtYzMyNTdlN2JkNTk5IiwiZXhwIjoxNzEwMDc3OTk1fQ.cU4qNeDiF-C6VYmMmpQKCV6HBl-nUaRILeB5uQU8_Oo"
    }


## Employee Endpoint
### Get All Employees
#### Endpoint: http://127.0.0.1:5000/employee
#### Method: GET
#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "DateOfBirth": "2001-05-14",
        "DepartmentID": 101,
        "Email": "rahul@gmail.com",
        "EmployeeID": 1,
        "FirstName": "rahul",
        "HireOfDate": "2022-03-12",
        "LastName": "barolia",
        "ManagerID": 1,
        "PhoneNumber": "1212567895",
        "Position": "Marketing Manager"
    }

### Get Employee By Id
#### Endpoint: http://127.0.0.1:5000/employee?EmployeeID=2
#### Method: GET
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `EmployeeID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "DateOfBirth": "2001-05-15",
        "DepartmentID": 102,
        "Email": "sahil@gmail.com",
        "EmployeeID": 2,
        "FirstName": "sahil",
        "HireOfDate": "2022-03-13",
        "LastName": "barolia",
        "ManagerID": 2,
        "PhoneNumber": "1212567896",
        "Position": "Account Executive"
    }


### Add Employee
#### Endpoint: http://127.0.0.1:5000/employee
#### Method: POST
#### Headers : Authorization (string): Bearer token obtained from login.
#### Body
    {
        "DateOfBirth": "2001-05-15",
        "DepartmentID": 102,
        "Email": "sahil@gmail.com",
        "EmployeeID": 2,
        "FirstName": "sahil",
        "HireOfDate": "2022-03-13",
        "LastName": "barolia",
        "ManagerID": 2,
        "PhoneNumber": "1212567896",
        "Position": "Account Executive"
    }
#### Response
    {
        "message":"data added successfully"
    }

### Update Employee
#### Endpoint: http://127.0.0.1:5000/employee?EmployeeID=2
#### Method: PUT
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `EmployeeID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.


#### Body
    {
        "DateOfBirth": "2001-05-15",
        "DepartmentID": 102,
        "Email": "sahil@gmail.com",
        "FirstName": "sahil",
        "HireOfDate": "2022-03-13",
        "LastName": "barolia",
        "ManagerID": 2,
        "PhoneNumber": "1212567896",
        "Position": "Account Executive"
    }
#### Response
    {
        "message":"data update successfully"
    }

### Delete Employee
#### Endpoint: http://127.0.0.1:5000/employee?EmployeeID=2
#### Method: DELETE
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `EmployeeID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "message": "data deleted"
    }


## Address Endpoint
### Get All Employees Address
#### Endpoint: http://127.0.0.1:5000/employee/address
#### Method: GET
#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "AddressID": 1,
        "Employee_ref_ID": 1,
        "city_id": 1,
        "country_id": 1,
        "state_id": 1,
        "street": "123 near a",
        "zipcode": "21222"
    }

### Get address By Id
#### Endpoint: http://127.0.0.1:5000/employee/address?AddressID=1
#### Method: GET
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `AddressID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "AddressID": 1,
        "Employee_ref_ID": 1,
        "city_id": 1,
        "country_id": 1,
        "state_id": 1,
        "street": "123 near a",
        "zipcode": "21222"
    }

### Add Address of Employee
#### Endpoint: http://127.0.0.1:5000/employee/address
#### Method: POST
#### Headers : Authorization (string): Bearer token obtained from login.
#### Body
    {
        "AddressID": 3,
        "City": "Townton",
        "EmployeeID": 3,
        "State": "Stateville",
        "Street": "456 Oak St",
        "Zipcode": "56789"
    }

#### Response
    {
        "message":"data added successfully"
    }    

### Update Employee Address
#### Endpoint: http://127.0.0.1:5000/employee/address?AddressID=3
#### Method: PUT
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `AddressID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.

#### Body
    {
        "City": "Townton",
        "EmployeeID": 3,
        "State": "Stateville",
        "Street": "456 Oak St",
        "Zipcode": "56789"
    }
#### Response
    {
        "message":"data update successfully"
    }


### Delete Employee Address
#### Endpoint: http://127.0.0.1:5000/employee/address?AddressID=3
#### Method: DELETE
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `AddressID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "message": "data deleted"
    }


## Salary Endpoint
### Get All Employees Salary
#### Endpoint: http://127.0.0.1:5000/employee/salary
#### Method: GET
#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "EmployeeID": 1,
        "Salary": 75000,
        "SalaryID": 1
    }

### Get salary By Id
#### Endpoint: http://127.0.0.1:5000/employee/salary?SalaryID=2
#### Method: GET
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `AddressID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "EmployeeID": 1,
        "Salary": 75000,
        "SalaryID": 1
    }

### Add salary of Employee
#### Endpoint: http://127.0.0.1:5000/employee/salary
#### Method: POST
#### Headers : Authorization (string): Bearer token obtained from login.
#### Body
    {
        "EmployeeID": 1,
        "Salary": 75000,
        "SalaryID": 1
    }

#### Response
    {
        "message":"data added successfully"
    }

### Update Employee Salary
#### Endpoint: http://127.0.0.1:5000/employee/salary?SalaryID=2
#### Method: PUT
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `SalaryID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.

#### Body
    {
        "EmployeeID": 1,
        "Salary": 75000,
    }

#### Response
    {
        "message":"data update successfully"
    }


### Delete Employee salary
#### Endpoint:http://127.0.0.1:5000/employee/salary?SalaryID=2
#### Method: DELETE
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `SalaryID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "message": "data deleted"
    }


## Department Endpoint
### Get All Employees Department
#### Endpoint: http://127.0.0.1:5000/employee/department
#### Method: GET
#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "DepartmentID": 101,
        "DepartmentName": "Marketing"
    }

### Get department By Id
#### Endpoint: http://127.0.0.1:5000/employee/department?DepartmentID=101
#### Method: GET
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `DepartmentID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "DepartmentID": 101,
        "DepartmentName": "Marketing"
    }


### Add department of Employee
#### Endpoint: http://127.0.0.1:5000/employee/department
#### Method: POST
#### Headers : Authorization (string): Bearer token obtained from login.
#### Body
    {
        "DepartmentID": 101,
        "DepartmentName": "Marketing"
    }

#### Response
    {
        "message":"data added successfully"
    }

### Update Employee department
#### Endpoint: http://127.0.0.1:5000/employee/department?DepartmentID=101
#### Method: PUT
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `DepartmentID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.

#### Body
    {
        "DepartmentName": "Sale"
    }

#### Response
    {
        "message":"data update successfully"
    }


### Delete Employee department
#### Endpoint:http://127.0.0.1:5000/employee/department?DepartmentID=101
#### Method: DELETE
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `DepartmentID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "message": "data deleted"
    }



## Project Endpoint
### Get All Employees Project
#### Endpoint: http://127.0.0.1:5000/employee/project
#### Method: GET
#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "Budget": 30000,
        "DepartmentID": 101,
        "EmployeeID": 1,
        "EndDate": "2022-05-25",
        "ProjectID": 1,
        "ProjectName": "xyzfgrgrgrd",
        "StartDate": "2022-04-20",
        "Status": "Complete"
    }

### Get project By Id
#### Endpoint: http://127.0.0.1:5000/employee/project?ProjectID=1
#### Method: GET
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `ProjectID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "Budget": 30000,
        "DepartmentID": 101,
        "EmployeeID": 1,
        "EndDate": "2022-05-25",
        "ProjectID": 1,
        "ProjectName": "xyzfgrgrgrd",
        "StartDate": "2022-04-20",
        "Status": "Complete"
    }


### Add project of Employee
#### Endpoint: http://127.0.0.1:5000/employee/project
#### Method: POST
#### Headers : Authorization (string): Bearer token obtained from login.
#### Body
    {
        "Budget": 30000,
        "DepartmentID": 101,
        "EmployeeID": 1,
        "EndDate": "2022-05-25",
        "ProjectID": 1,
        "ProjectName": "xyzfgrgrgrd",
        "StartDate": "2022-04-20",
        "Status": "Complete"
    }

#### Response
    {
        "message":"data added successfully"
    }

### Update Employee project
#### Endpoint: http://127.0.0.1:5000/employee/project?ProjectID=1
#### Method: PUT
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `ProjectID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.

#### Body
    {
        "Budget": 30000,
        "DepartmentID": 101,
        "EmployeeID": 1,
        "EndDate": "2022-05-25",
        "ProjectName": "xyzfgrgrgrd",
        "StartDate": "2022-04-20",
        "Status": "Complete"
    }

#### Response
    {
        "message":"data update successfully"
    }


### Delete Employee project
#### Endpoint:http://127.0.0.1:5000/employee/project?ProjectID=1
#### Method: DELETE
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `ProjectID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "message": "data deleted"
    }




## Qualification Endpoint
### Get All Employees Qualification
#### Endpoint: http://127.0.0.1:5000/employee/qualification
#### Method: GET
#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "Degree": "xyz degree",
        "EmployeeID": 1,
        "GraduationYear": 2016,
        "Institute": "xyz University",
        "QualificationID": 1
    }

### Get Qualification By Id
#### Endpoint: http://127.0.0.1:5000/employee/qualification?QualificationID=1
#### Method: GET
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `QualificationID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "Degree": "xyz degree",
        "EmployeeID": 1,
        "GraduationYear": 2016,
        "Institute": "xyz University",
        "QualificationID": 1
    }


### Add Qualification of Employee
#### Endpoint: http://127.0.0.1:5000/employee/qualification
#### Method: POST
#### Headers : Authorization (string): Bearer token obtained from login.
#### Body
    {
        "Degree": "xyz degree",
        "EmployeeID": 1,
        "GraduationYear": 2016,
        "Institute": "xyz University",
        "QualificationID": 1
    }

#### Response
    {
        "message":"data added successfully"
    }

### Update Employee Qualification
#### Endpoint: http://127.0.0.1:5000/employee/qualification?QualificationID=1
#### Method: PUT
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `QualificationID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.

#### Body
    {
        "Degree": "xyz degree",
        "EmployeeID": 1,
        "GraduationYear": 2016,
        "Institute": "xyz University",
        "QualificationID": 1
    }

#### Response
    {
        "message":"data update successfully"
    }


### Delete Employee Qualification
#### Endpoint:http://127.0.0.1:5000/employee/qualification?QualificationID=1
#### Method: DELETE
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `QualificationID` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    {
        "message": "data deleted"
    }


### Get nth highest salary of employee
#### Endpoint: http://127.0.0.1:5000/employee/nthSalary?Rank=1
#### Method: GET
#### Parameter:
| Key | Value    | Description                |
| :-------- | :------- | :------------------------- |
| `Rank` | `int` | **Required**. Your API key |

#### Headers : Authorization (string): Bearer token obtained from login.
#### Response
    [
        {
            "Employee_salary": 84000
        }
    ]

