def get_or_insert_Department(cursor,conn,department_name):
    """
        this function retrives the department id if it exist and if not exist then insert a new department with the given 
        department and return generated department id
    """
    
    department_id=get_department_id(cursor,department_name)
    if not department_id:
        department_id = insert_department(cursor,conn,department_name)
    return department_id

def get_department_id(cursor,department_name):
    """
        this function retrives the department id for a given department name from the department table and return the department
        id if it exist otherwise return none
    """
    
    query = f"SELECT DepartmentID FROM Department WHERE DepartmentName = '{department_name}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def insert_department(cursor,conn,department_name):
    """
        this function insert a new department and retrives the department id from the department table that is currently insert
        a new record 
    """
    
    query = f"INSERT INTO Department(DepartmentName) VALUES ('{department_name}')"
    cursor.execute(query)
    conn.commit()
    query = "SELECT SCOPE_IDENTITY()"
    cursor.execute(query)
    department_id = cursor.fetchone()[0]
    return department_id

def is_employee_exists(cursor,row):
    """
        this function checks if an employee with the given first name, last name, and email already exists in
        the Employee table. It returns 1 if the employee exists and 0 otherwise.
    """

    query = f"SELECT COUNT(*) FROM Employee WHERE Email ='{row['Email']}' AND PhoneNumber='{row['PhoneNumber']}' "
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0] > 0

def insert_employee(cursor,conn,row,department_id):
        """
            This function inserts a new employee into the Employee table with the provided data.It takes the employee
            information from the row and inserts it into the table
        """
        query2=f"""
                    INSERT INTO Employee(FirstName,LastName,DateOfBirth,
                    HireOfDate,Email,PhoneNumber,Position,DepartmentID,ManagerID) values('{row['FirstName']}','{row['LastName']}','{row['DateOfBirth']}',
                    '{row['HireOfDate']}','{row['Email']}',{row['PhoneNumber']},'{row['Position']}',{department_id},null)
                    
                """ 
        cursor.execute(query2)
        conn.commit()
 

def get_employee_id(cursor,firstname,phone,Email):
    """
        This function retrieves the EmployeeID for an employee based on the provided first name,
        phone number, and email.
    """
    
    query = f"SELECT EmployeeID FROM Employee WHERE FirstName = '{firstname}' AND PhoneNumber = '{phone}' AND Email='{Email}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def insert_address(cursor,conn,row, employee_id):
    """
        This function inserts address data into the Address table. It first retrieves or inserts the 
        corresponding country, state, and city IDs using helper functions, and then inserts the address
        data into the Address table along with the retrieved IDs.
    """

    country_id = get_or_insert_country(cursor,conn,row['CountryName'])
    state_id = get_or_insert_state(cursor,conn,row['State Name'])
    city_id = get_or_insert_city(cursor,conn,row['CityName'])
    
    query3=f"""
                    INSERT INTO Address(Employee_ref_ID,country_id,state_id,city_id,street,Zipcode)
                    values({employee_id},
                    {country_id},{state_id},{city_id},'{(row['StreetName'])}','{row['Zipcode']}')
                    
                """
    cursor.execute(query3)
    conn.commit()

def get_or_insert_country(cursor,conn,country_name):
    """
        Check if the country exists, if not, insert it and return its ID
    """
    
    query = f"SELECT country_id FROM Country WHERE CountryName = '{country_name}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        query = f"INSERT INTO Country(CountryName) VALUES ('{country_name}')"
        cursor.execute(query)
        conn.commit()
        query = "SELECT SCOPE_IDENTITY()"
        cursor.execute(query)
        country_id = cursor.fetchone()[0]
        return country_id

def get_or_insert_state(cursor,conn,state_name):
    """
        Check if the state exists, if not, insert it and return its ID
    """
    query = f"SELECT state_id FROM State WHERE state_name = '{state_name}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        query =f"INSERT INTO State(state_name) VALUES ('{state_name}')"
        cursor.execute(query)
        conn.commit()
        query = "SELECT SCOPE_IDENTITY()"
        cursor.execute(query)
        state_id = cursor.fetchone()[0]
        return state_id

def get_or_insert_city(cursor,conn,city_name):
    """
        Check if the city exists, if not, insert it and return its ID
    """
    
    query =f"SELECT city_id FROM City WHERE city_name = '{city_name}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        query = f"INSERT INTO City(city_name) VALUES ('{city_name}')"
        cursor.execute(query)
        conn.commit()
        query = "SELECT SCOPE_IDENTITY()"
        cursor.execute(query)
        city_id = cursor.fetchone()[0]
        return city_id


def insert_salary(cursor,conn,row,employee_id):
    """
        insert salary data for an employee into the salary table
    """
    
    query = f"SELECT COUNT(*) FROM Salary WHERE EmployeeID = {employee_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    if result[0] == 0:
        query4=f"INSERT INTO Salary(EmployeeID,Salary) values({employee_id},{int(row['Salary'])})"
        cursor.execute(query4)
        conn.commit()
        
def insert_qualification(cursor,conn,row,employee_id):
    """
        insert qualification data for an employee into the qualification table
    """
    
    query=f"""  
                    INSERT INTO Qualification(EmployeeID,Degree,GraduationYear,Institute)
                    values({employee_id},'{row['Degree']}',{int(row['GraduationYear'])},'{row['Institute']}')
                    
                """
    cursor.execute(query)
    conn.commit()
    
def insert_project(cursor,conn,row,employee_id,department_id):
    """
        insert project data for an employee into the project table
    """
    
    query5=f""" 
                    INSERT INTO Project(EmployeeID,DepartmentID,ProjectName,StartDate,EndDate,Budget,Status)
                    values({employee_id},
                    {department_id},'{row['ProjectName']}','{row['StartDate']}','{row['EndDate']}',{int(row['Budget'])},'{row['Status']}')
                    
                """   

    cursor.execute(query5)
    conn.commit()
