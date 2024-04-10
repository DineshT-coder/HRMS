import pyodbc

class DataBaseConnectivity:
    """Class to establish database connectivity and provide cursor for executing queries."""

    def __init__(self):
        """Initialize the database connection and cursor."""
        
        self.conn=pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-KGD64VN9;DATABASE=employeeinformation;')
        self.cursor=self.conn.cursor()
    
class EmployeeInformation(DataBaseConnectivity):
    """
    Class to manage employee information in the database
    """
    
    def getAllEmployeeRecord(self):
        """
        Retrieve all employee records from the database
        """
        result=[]
        query="SELECT * FROM Employee"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            employee_dict={}
            employee_dict['EmployeeID']=row[0]
            employee_dict['FirstName']=row[1]
            employee_dict['LastName']=row[2]
            employee_dict['DateOfBirth']=row[3]
            employee_dict['HireOfDate']=row[4]
            employee_dict['Email']=row[5]
            employee_dict['PhoneNumber']=row[6]
            employee_dict['DepartmentID']=row[7]
            employee_dict['Position']=row[8]
            employee_dict['ManagerID']=row[9]
            result.append(employee_dict)
        return result
    
    def getParticularEmployeeRecord(self,id):
        """Retrieve a particular employee record from the database"""
        
        query=f"SELECT * FROM Employee WHERE EmployeeID={id}"        
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            employee_dict={}
            employee_dict['EmployeeID']=row[0]
            employee_dict['FirstName']=row[1]
            employee_dict['LastName']=row[2]
            employee_dict['DateOfBirth']=row[3]
            employee_dict['HireOfDate']=row[4]
            employee_dict['Email']=row[5]
            employee_dict['PhoneNumber']=row[6]
            employee_dict['DepartmentID']=row[7]
            employee_dict['Position']=row[8]
            employee_dict['ManagerID']=row[9]
            return([employee_dict])
        
    def addEmployeeRecord(self,data):
        """Add a new employee record to the database."""
        
        query2=f"""
                    INSERT INTO Employee(FirstName,LastName,DateOfBirth,
                    HireOfDate,Email,PhoneNumber,Position,DepartmentID) values('{data['FirstName']}',
                    '{data['LastName']}','{data['DateOfBirth']}',
                    '{data['HireOfDate']}','{data['Email']}','{data['PhoneNumber']}',
                    '{data['Position']}',{data['DepartmentID']})
                    
                """ 
        self.cursor.execute(query2)
        self.conn.commit()
        
        # query for manager id
        q=f"""
                UPDATE t1
                SET t1.managerid = t2.employeeid
                FROM Employee t1
                JOIN Employee t2 ON t1.EmployeeID = t2.EmployeeID;
                
            """
        self.cursor.execute(q)
        self.conn.commit()
        
        employee_id_fetch=f'select SCOPE_IDENTITY();'
        employee_id=self.cursor.execute(employee_id_fetch).fetchone()[0]
        return employee_id
        
        
    def updateEmployeeRecord(self,empid,data):
        """Update an existing employee record in the database."""
        
        query=f"""  
                    UPDATE Employee SET FirstName='{data['FirstName']}',LastName='{data['LastName']}',
                    DateOfBirth='{data['DateOfBirth']}',HireOfDate='{data['HireOfDate']}',
                    Email='{data['Email']}',PhoneNumber='{data['PhoneNumber']}',
                    DepartmentID={data['DepartmentID']},
                    Position='{data['Position']}',ManagerID={data['ManagerID']} WHERE EmployeeID={empid}
                    
                """
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
    def employee_patch_method(self,id,data):
        """Partially update an employee record in the database."""

        query="UPDATE Employee SET "
        for key in data:
            # 
            if isinstance(data[key], str):
                query += f"{key}='{data[key]}', "
            else:
                query += f"{key}={data[key]}, "
        
        query=query[:-2]+f" Where EmployeeID={id}"
        print(query)
        self.cursor.execute(query)
        
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
            
    # def deleteEmployeeRecord(self,empid):
    #     query=f"DELETE FROM Employee WHERE EmployeeID={empid}"
    #     self.cursor.execute(query)
    #     if self.cursor.rowcount!=0:
    #         self.conn.commit()
    #         return True
    #     else:
    #         return False
    
    def deleteEmployeeRecord(self,empid):
        """Delete an employee record from the database."""
        
        # query_city=f"delete from city where not exists(select 1 from Address where city.city_id=Address.AddressID)"
        # self.cursor.execute(query_city)
        # self.conn.commit()
        
        # query_state=f"delete from State where not exists(select 1 from Address where STATE.state_id=Address.AddressID)"
        # self.cursor.execute(query_state)
        # self.conn.commit()
        
        # query_country=f"delete from Country where not exists(select 1 from Address where Country.country_id=Address.AddressID)"
        # self.cursor.execute(query_country)
        # self.conn.commit()
        
        query_department=f"delete from department where not exists(select 1 from employee where employee.DepartmentID=Department.DepartmentID)"
        self.cursor.execute(query_department)
        self.conn.commit()
        
        query=f"DELETE FROM Employee WHERE EmployeeID={empid}"
        self.cursor.execute(query)
        
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
    
        
        
        
class Address(DataBaseConnectivity):
    """Class to manage employee addresses in the database."""
    
    def getAllEmployeeAddress(self):
        """Retrieve all employee addresses from the database."""
        
        result=[]
        query="SELECT * FROM Address"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            address_dict={}
            address_dict['AddressID']=row[0]
            address_dict['Employee_ref_ID']=row[1]
            address_dict['country_id']=row[2]
            address_dict['state_id']=row[3]
            address_dict['city_id']=row[4]
            address_dict['street']=row[5]
            address_dict['zipcode']=row[6]
            result.append(address_dict)
        return result
    
    def getParticularEmployeeAddress(self,addressid):
        """Retrieve a particular employee address from the database."""
        
        query=f"SELECT * FROM Address WHERE AddressID={addressid}"        
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            address_dict={}
            address_dict['AddressID']=row[0]
            address_dict['Employee_ref_ID']=row[1]
            address_dict['country_id']=row[2]
            address_dict['state_id']=row[3]
            address_dict['city_id']=row[4]
            address_dict['street']=row[5]
            address_dict['zipcode']=row[6]
            return([address_dict])
        
    def addEmployeeAddress(self,data):
        """Add a new employee address record to the database."""
        
        query=f"""INSERT INTO Address(Employee_ref_ID,country_id,state_id,city_id,street,zipcode) VALUES(
            {data['Employee_ref_ID']},{data['country_id']},{data['state_id']},{data['city_id']},'{data['street']}',
                '{data['zipcode']}')"""
        self.cursor.execute(query)
        self.conn.commit()    
    
    def updateEmployeeAddress(self,addid,data):
        """Update an existing employee address record in the database."""

        query=f"""UPDATE Address SET Employee_ref_ID={data['Employee_ref_ID']},country_id={data['country_id']}
            ,state_id={data['state_id']},city_id={data['city_id']},street='{data['street']}',zipcode='{data['zipcode']}'
            WHERE AddressID={addid}"""
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
            
    def deleteEmployeeAddress(self,addid):
        """Delete an employee address record from the database."""
        
        query=f"DELETE FROM Address WHERE AddressID={addid}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
  
class Country(DataBaseConnectivity):
    """Class to manage employee countries in the database."""

    def getAllEmployeeCountry(self):
        """Retrieve all employee countries from the database."""
        
        result=[]
        query="SELECT * FROM Country"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            country_dict={}
            country_dict['country_id']=row[0]
            country_dict['countryName']=row[1]
            result.append(country_dict)
        return result
    
    def getParticularEmployeeCountry(self,country_id):
        """Retrieve a particular employee country from the database."""
        
        query=f"SELECT * FROM Country WHERE country_id={country_id}"        
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            country_dict={}
            country_dict['country_id']=row[0]
            country_dict['countryName']=row[1]
            return([country_dict])
        
    def addEmployeeCountry(self,data):
        """Add a new employee country record to the database."""
        
        query=f"INSERT INTO Country(countryName) VALUES('{data['countryName']}')"
        self.cursor.execute(query)
        self.conn.commit()    
    
    def updateEmployeeCountry(self,country_id,data):
        """Update an existing employee country record in the database."""
        
        query=f"UPDATE Country SET countryName='{data['countryName']}' WHERE country_id={country_id}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
            
    def deleteEmployeeCountry(self,country_id):
        """Delete an employee country record from the database."""
        
        query=f"DELETE FROM Country WHERE country_id={country_id}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
      
class State(DataBaseConnectivity):
    """Class to manage employee states in the database."""
    
    def getAllEmployeeState(self):
        """Retrieve all employee states from the database."""
        
        result=[]
        query="SELECT * FROM State"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            state_dict={}
            state_dict['state_id']=row[0]
            state_dict['state_name']=row[1]
            result.append(state_dict)
        return result
    
    def getParticularEmployeeState(self,state_id):
        """Retrieve a particular employee state from the database."""
        
        query=f"SELECT * FROM State WHERE state_id={state_id}"        
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            state_dict={}
            state_dict['state_id']=row[0]
            state_dict['state_name']=row[1]
            return([state_dict])
        
    def addEmployeeState(self,data):
        """Add a new employee state record to the database."""
        
        query=f"INSERT INTO State VALUES('{data['state_name']}')"
        self.cursor.execute(query)
        self.conn.commit()    
    
    def updateEmployeeState(self,state_id,data):
        """Update an existing employee state record in the database."""
        
        query=f"UPDATE State SET state_name='{data['state_name']}' WHERE state_id={state_id}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
            
    def deleteEmployeeState(self,state_id):
        """Delete an employee state record from the database."""
        
        query=f"DELETE FROM State WHERE state_id={state_id}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
      

class City(DataBaseConnectivity):
    """Class to manage employee cities in the database."""
    
    def getAllEmployeeCity(self):
        """Retrieve all employee cities from the database."""

        result=[]
        query="SELECT * FROM City"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            city_dict={}
            city_dict['city_id']=row[0]
            city_dict['city_name']=row[1]
            result.append(city_dict)
        return result
    
    def getParticularEmployeeCity(self,city_id):
        """Retrieve a particular employee city from the database."""
        
        query=f"SELECT * FROM City WHERE city_id={city_id}"        
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            city_dict={}
            city_dict['city_id']=row[0]
            city_dict['city_name']=row[1]
            return([city_dict])
        
    def addEmployeeCity(self,data):
        """Add a new employee city record to the database."""
        
        query=f"INSERT INTO City(city_name) VALUES('{data['city_name']}')"
        self.cursor.execute(query)
        self.conn.commit()    
    
    def updateEmployeeCity(self,city_id,data):
        """Update an existing employee city record in the database."""
        
        query=f"UPDATE City SET city_name='{data['city_name']}' WHERE city_id={city_id}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
            
    def deleteEmployeeCity(self,city_id):
        """Delete an employee city record from the database."""
        
        query=f"DELETE FROM City WHERE city_id={city_id}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
      
    

class Department(DataBaseConnectivity):
    """Class to manage employee departments in the database."""
    
    def getAllEmployeeDepartment(self):
        """Retrieve all employee departments from the database."""
        
        result=[]
        query="SELECT * FROM Department"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            department_dict={}
            department_dict['DepartmentID']=row[0]
            department_dict['DepartmentName']=row[1]
            result.append(department_dict)
            # print(result)
        return result
    
    def getParticularEmployeeDepartment(self,depid):
        """Retrieve a particular employee department from the database"""
         
        query=f"SELECT * FROM Department WHERE DepartmentID={depid}"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            department_dict={}
            department_dict['DepartmentID']=row[0]
            department_dict['DepartmentName']=row[1]
            return([department_dict])
        
    def addEmployeedepartment(self,data):
        """Add a new employee department record to the database."""
        query=f"INSERT INTO Department VALUES('{data['DepartmentName']}')"
        self.cursor.execute(query)
        self.conn.commit()
     
    def updateEmployeeDepartment(self,depid,data):
        """Update an existing employee department record in the database."""
        
        query=f"UPDATE Department SET DepartmentName='{data['DepartmentName']}' WHERE DepartmentID={depid}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
    
    def deleteEmployeeDepartment(self,depid):
        """Delete an employee department record from the database."""
        
        query=f"DELETE FROM Department WHERE DepartmentID={depid}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:return False
        
class Qualification(DataBaseConnectivity):
    """Class to manage employee qualifications in the database."""
    
    def getAllEmployeeQualification(self):
        """Retrieve all employee qualifications from the database"""
        
        result=[]
        query=f"SELECT * FROM Qualification"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            qualification_dict={}
            qualification_dict['QualificationID']=row[0]
            qualification_dict['EmployeeID']=row[1]
            qualification_dict['Degree']=row[2]
            qualification_dict['GraduationYear']=row[3]
            qualification_dict['Institute']=row[4]
            result.append(qualification_dict)
        return result
    
    def getParticularEmployeeQualification(self,id):
        """Retrieve a particular employee qualification from the database."""
        
        query=f"SELECT * FROM Qualification WHERE QualificationID={id}"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            qualification_dict={}
            qualification_dict['QualificationID']=row[0]
            qualification_dict['EmployeeID']=row[1]
            qualification_dict['Degree']=row[2]
            qualification_dict['GraduationYear']=row[3]
            qualification_dict['Institute']=row[4]
            return([qualification_dict])
        
    def updateEmployeeQualification(self,id,data):
        """Update an existing employee qualification record in the database."""
        
        query=f"""UPDATE Qualification SET Degree='{data['Degree']}',
        GraduationYear={data['GraduationYear']},
        Institute='{data['Institute']}',EmployeeID={data['EmployeeID']}  WHERE QualificationID={id}"""
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        

    def  addEmployeeQualification(self,data):
        """Add a new employee qualification record to the database."""
        
        query=f"""INSERT INTO Qualification(EmployeeID,Degree,GraduationYear,Institute) 
        VALUES({data['EmployeeID']},'{data['Degree']}',{data['GraduationYear']},'{data['Institute']}')"""
        self.cursor.execute(query)
        self.conn.commit()
    
    def deleteEmployeeQualification(self,id):
        """Delete an employee qualification record from the database."""
        
        query=f"DELETE FROM Qualification WHERE QualificationID={id}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False

class Salary(DataBaseConnectivity):
    """Class to manage employee salaries in the database."""
    
    def getAllEmployeeSalary(self):
        """Retrieve all employee salaries from the database."""
        
        result=[]
        query="SELECT * FROM Salary"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            salary_dict={}
            salary_dict['SalaryID']=row[0]
            salary_dict['EmployeeID']=row[1]
            salary_dict['Salary']=row[2]
            result.append(salary_dict)
            # print(result)
        return result
    
    def getParticularEmployeeSalary(self,salaryid):
        """Retrieve a particular employee salary from the database."""
        
        query=f"SELECT * FROM Salary WHERE SalaryID={salaryid}"        
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            salary_dict={}
            salary_dict['SalaryID']=row[0]
            salary_dict['EmployeeID']=row[1]
            salary_dict['Salary']=row[2]
            return([salary_dict])
        
    def  addEmployeeSalary(self,data):
        """Add a new employee salary record to the database."""
        
        query=f"INSERT INTO Salary(EmployeeID,Salary) VALUES({data['EmployeeID']},{data['Salary']})"
        self.cursor.execute(query)
        self.conn.commit()
        
    def updateEmployeeSalary(self,salaryid,data):
        """Update an existing employee salary record in the database."""

        query=f"UPDATE Salary SET EmployeeID={data['EmployeeID']},\
            Salary={data['Salary']} WHERE SalaryID={salaryid}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False

            
    def deleteEmployeeSalary(self,salaryid):
        """delete an existing employee salary record in the database.  """

        query=f"DELETE FROM Salary WHERE SalaryID={salaryid}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
class Project(DataBaseConnectivity):
    """Class to manage projects in the database."""
    
    def getAllProject(self):
        """Retrieve all projects from the database."""
        
        result=[]
        query="SELECT * FROM Project"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            project_dict={}
            project_dict['ProjectID']=row[0]
            project_dict['EmployeeID']=row[1]
            project_dict['DepartmentID']=row[2]
            project_dict['ProjectName']=row[3]
            project_dict['StartDate']=row[4]
            project_dict['EndDate']=row[5]
            project_dict['Budget']=row[6]
            project_dict['Status']=row[7]
            result.append(project_dict)
        return result
    
    def getParticularProject(self,projectid):
        """Retrieve a particular project from the database."""
        
        query=f"SELECT * FROM Project WHERE ProjectID={projectid}"        
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            project_dict={}
            project_dict['ProjectID']=row[0]
            project_dict['EmployeeID']=row[1]
            project_dict['DepartmentID']=row[2]
            project_dict['ProjectName']=row[3]
            project_dict['StartDate']=row[4]
            project_dict['EndDate']=row[5]
            project_dict['Budget']=row[6]
            project_dict['Status']=row[7]
            return([project_dict])
        
    def  addProject(self,data):
        """Add a new project record to the database."""

        query=f"""INSERT INTO Project(ProjectName,StartDate,EndDate,Budget,Status,DepartmentID,EmployeeID) VALUES('{data['ProjectName']}','{data['StartDate']}',
            '{data['EndDate']}',{data['Budget']},'{data['Status']}',{data['DepartmentID']},{data['EmployeeID']})"""
        self.cursor.execute(query)
        self.conn.commit()
        
    def updateProject(self,projectid,data):
        """Update an existing project record in the database."""
        
        query=f"""UPDATE Project SET ProjectName='{data['ProjectName']}',
            StartDate='{data['StartDate']}',EndDate='{data['EndDate']}',EmployeeID={data['EmployeeID']},
                Budget={data['Budget']},DepartmentID={data['DepartmentID']},
                    Status='{data['Status']}' WHERE ProjectID={projectid}"""
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
        
    def deleteProject(self,projectid):
        """Delete a project record from the database."""
        
        query=f"DELETE FROM Project WHERE ProjectID={projectid}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
class EmployeeNthSalary(DataBaseConnectivity):
    """Class to retrieve the nth highest salary of employees from the database."""
    
    def getAllEmployeeRecord(self,rank):
        """Retrieve the nth highest salary from the database."""
        
        query=f"""with combinedata as (select Employee.EmployeeID,FirstName,LastName,DateOfBirth,
                HireOfDate,Email,PhoneNumber,DepartmentID,
                Position,ManagerID,SalaryID,Salary
                from employee join salary
                on employee.employeeid=salary.employeeid)
                SELECT distinct (salary)
                FROM combinedata
                ORDER BY salary DESC
                OFFSET {rank-1} ROWS
                FETCH NEXT 1 ROWS ONLY;"""
        self.cursor.execute(query)
        result=[]
        for row in self.cursor.fetchall():
            employee_dict={}
            employee_dict['Employee_salary']=row[0]
            result.append(employee_dict)
#             # print(result)
        return result
        