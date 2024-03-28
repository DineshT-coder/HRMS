import pyodbc

class DataBaseConnectivity:
    def __init__(self):
        self.conn=pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-KGD64VN9;DATABASE=employeeinformation;')
        self.cursor=self.conn.cursor()
    
class EmployeeInformation(DataBaseConnectivity):
    def getAllEmployeeRecord(self):
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
        
        
    def updateEmployeeRecord(self,empid,data):
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
            
    # def deleteEmployeeRecord(self,empid):
    #     query=f"DELETE FROM Employee WHERE EmployeeID={empid}"
    #     self.cursor.execute(query)
    #     if self.cursor.rowcount!=0:
    #         self.conn.commit()
    #         return True
    #     else:
    #         return False
    
    def deleteEmployeeRecord(self,empid):
        
        
        query_city=f"delete from city where not exists(select 1 from Address where city.city_id=Address.AddressID)"
        self.cursor.execute(query_city)
        self.conn.commit()
        
        query_state=f"delete from State where not exists(select 1 from Address where STATE.state_id=Address.AddressID)"
        self.cursor.execute(query_state)
        self.conn.commit()
        
        query_country=f"delete from Country where not exists(select 1 from Address where Country.country_id=Address.AddressID)"
        self.cursor.execute(query_country)
        self.conn.commit()
        
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
    def getAllEmployeeAddress(self):
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
        query=f"""INSERT INTO Address(Employee_ref_ID,country_id,state_id,city_id,street,zipcode) VALUES(
            {data['Employee_ref_ID']},{data['country_id']},{data['state_id']},{data['city_id']},'{data['street']}',
                '{data['zipcode']}')"""
        self.cursor.execute(query)
        self.conn.commit()    
    
    def updateEmployeeAddress(self,addid,data):
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
        query=f"DELETE FROM Address WHERE AddressID={addid}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
  
class Country(DataBaseConnectivity):
    def getAllEmployeeCountry(self):
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
        query=f"SELECT * FROM Country WHERE country_id={country_id}"        
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            country_dict={}
            country_dict['country_id']=row[0]
            country_dict['countryName']=row[1]
            return([country_dict])
        
    def addEmployeeCountry(self,data):
        query=f"INSERT INTO Country(countryName) VALUES('{data['countryName']}')"
        self.cursor.execute(query)
        self.conn.commit()    
    
    def updateEmployeeCountry(self,country_id,data):
        query=f"UPDATE Country SET countryName='{data['countryName']}' WHERE country_id={country_id}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
            
    def deleteEmployeeCountry(self,country_id):
        query=f"DELETE FROM Country WHERE country_id={country_id}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
      
class State(DataBaseConnectivity):
    def getAllEmployeeState(self):
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
        query=f"SELECT * FROM State WHERE state_id={state_id}"        
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            state_dict={}
            state_dict['state_id']=row[0]
            state_dict['state_name']=row[1]
            return([state_dict])
        
    def addEmployeeState(self,data):
        query=f"INSERT INTO State VALUES('{data['state_name']}')"
        self.cursor.execute(query)
        self.conn.commit()    
    
    def updateEmployeeState(self,state_id,data):
        query=f"UPDATE State SET state_name='{data['state_name']}' WHERE state_id={state_id}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
            
    def deleteEmployeeState(self,state_id):
        query=f"DELETE FROM State WHERE state_id={state_id}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
      

class City(DataBaseConnectivity):
    def getAllEmployeeCity(self):
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
        query=f"SELECT * FROM City WHERE city_id={city_id}"        
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            city_dict={}
            city_dict['city_id']=row[0]
            city_dict['city_name']=row[1]
            return([city_dict])
        
    def addEmployeeCity(self,data):
        query=f"INSERT INTO City(city_name) VALUES('{data['city_name']}')"
        self.cursor.execute(query)
        self.conn.commit()    
    
    def updateEmployeeCity(self,city_id,data):
        query=f"UPDATE City SET city_name='{data['city_name']}' WHERE city_id={city_id}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
            
    def deleteEmployeeCity(self,city_id):
        query=f"DELETE FROM City WHERE city_id={city_id}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
      
    

class Department(DataBaseConnectivity):
    def getAllEmployeeDepartment(self):
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
        query=f"SELECT * FROM Department WHERE DepartmentID={depid}"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            department_dict={}
            department_dict['DepartmentID']=row[0]
            department_dict['DepartmentName']=row[1]
            return([department_dict])
        
    def addEmployeedepartment(self,data):
        query=f"INSERT INTO Department VALUES('{data['DepartmentName']}')"
        self.cursor.execute(query)
        self.conn.commit()
     
    def updateEmployeeDepartment(self,depid,data):
        query=f"UPDATE Department SET DepartmentName='{data['DepartmentName']}' WHERE DepartmentID={depid}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
    
    def deleteEmployeeDepartment(self,depid):
        query=f"DELETE FROM Department WHERE DepartmentID={depid}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:return False
        
class Qualification(DataBaseConnectivity):
    def getAllEmployeeQualification(self):
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
        query=f"""INSERT INTO Qualification(EmployeeID,Degree,GraduationYear,Institute) 
        VALUES({data['EmployeeID']},'{data['Degree']}',{data['GraduationYear']},'{data['Institute']}')"""
        self.cursor.execute(query)
        self.conn.commit()
    
    def deleteEmployeeQualification(self,id):
        query=f"DELETE FROM Qualification WHERE QualificationID={id}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False

class Salary(DataBaseConnectivity):
    def getAllEmployeeSalary(self):
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
        query=f"SELECT * FROM Salary WHERE SalaryID={salaryid}"        
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            salary_dict={}
            salary_dict['SalaryID']=row[0]
            salary_dict['EmployeeID']=row[1]
            salary_dict['Salary']=row[2]
            return([salary_dict])
        
    def  addEmployeeSalary(self,data):
        query=f"INSERT INTO Salary(EmployeeID,Salary) VALUES({data['EmployeeID']},{data['Salary']})"
        self.cursor.execute(query)
        self.conn.commit()
        
    def updateEmployeeSalary(self,salaryid,data):
        query=f"UPDATE Salary SET EmployeeID={data['EmployeeID']},\
            Salary={data['Salary']} WHERE SalaryID={salaryid}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False

            
    def deleteEmployeeSalary(self,salaryid):
        query=f"DELETE FROM Salary WHERE SalaryID={salaryid}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
class Project(DataBaseConnectivity):
    def getAllProject(self):
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
        query=f"""INSERT INTO Project(ProjectName,StartDate,EndDate,Budget,Status,DepartmentID,EmployeeID) VALUES('{data['ProjectName']}','{data['StartDate']}',
            '{data['EndDate']}',{data['Budget']},'{data['Status']}',{data['DepartmentID']},{data['EmployeeID']})"""
        self.cursor.execute(query)
        self.conn.commit()
        
    def updateProject(self,projectid,data):
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
        query=f"DELETE FROM Project WHERE ProjectID={projectid}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
class EmployeeNthSalary(DataBaseConnectivity):

    def getAllEmployeeRecord(self,rank):
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
        