from flask import Flask,request,render_template
from flask_smorest import Api
from resources.employee import blp
from resources.address import blp_address
from resources.salary import blp_salary
from resources.department import blp_department
from resources.qualification import blp_qualification
from resources.project import blp_project
from resources.nthhighestsalary import blp_employeeNthSalary
from resources.user import blp_user    
from resources.city import blp_city
from resources.country import blp_country
from resources.state import blp_state
from flask_jwt_extended import JWTManager
import pyodbc
import os
import pandas as pd

app=Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"]=True
app.config['API_TITLE']="Employee Rest API" 
app.config["API_VERSION"]="V1"
app.config["OPENAPI_VERSION"]="3.0.3"
app.config["JWT_SECRET_KEY"]="rahul@12345"

api=Api(app)
jwt=JWTManager(app)
api.register_blueprint(blp)
api.register_blueprint(blp_address)
api.register_blueprint(blp_salary)
api.register_blueprint(blp_department)
api.register_blueprint(blp_qualification)
api.register_blueprint(blp_project)
api.register_blueprint(blp_employeeNthSalary)
api.register_blueprint(blp_user)
api.register_blueprint(blp_state)
api.register_blueprint(blp_city)
api.register_blueprint(blp_country)


app.config['DEBUG']=True
UPLOAD_FOLDER='uploads'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER 

try:
    conn=pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-KGD64VN9;DATABASE=employeeinformation;')
    cursor=conn.cursor()
    print("successfully")
except:
    print("some problem arises")
    
@app.route('/employee/csvdata')  
def home():
    return render_template('index.html')

@app.route('/employee/csvdata',methods=['POST'])
def upload_files():
    upload_file=request.files['file']
    if upload_file.filename !='':   
        file_path=os.path.join(app.config['UPLOAD_FOLDER'],upload_file.filename)
        print(file_path)
        upload_file.save(file_path)
        parseCsv(file_path)
    return "upload successfully"

def parseCsv(file_path):
    csvData=pd.read_csv(file_path)
    for i,row in csvData.iterrows():
        row=tuple(row)
        
        query_department=f"INSERT INTO Department(DepartmentName) values('{row[6]}')"
        cursor.execute(query_department)
        conn.commit()
        
        # department id fetch from department table
        q=f'select SCOPE_IDENTITY();'
        department_value=cursor.execute(q).fetchone()[0]
        
    
        # emoployee
        query2=f"""
                    INSERT INTO Employee(FirstName,LastName,DateOfBirth,
                    HireOfDate,Email,PhoneNumber,Position,DepartmentID) values('{row[0]}','{row[1]}','{row[2]}',
                    '{row[3]}','{row[4]}',{row[5]},'{row[7]}',{department_value})
                    
                """ 
        cursor.execute(query2)
        conn.commit()
        # query for manager id
        q=f"""
                UPDATE t1
                SET t1.managerid = t2.employeeid
                FROM Employee t1
                JOIN Employee t2 ON t1.EmployeeID = t2.EmployeeID;
                
            """
        cursor.execute(q)
        conn.commit()
        
        # employee id fetch from employee table
        q=f'select SCOPE_IDENTITY();'
        employeeid_value=cursor.execute(q).fetchone()[0]
        
        
        
        # query for qualification
        query=f"""  
                    INSERT INTO Qualification(EmployeeID,Degree,GraduationYear,Institute)
                    values({employeeid_value},'{row[14]}',{int(row[15])},'{row[16]}')
                    
                """
        cursor.execute(query)
        conn.commit()
        
       
        #Country
        query_country=f"INSERT INTO Country values('{row[8]}')" 
        cursor.execute(query_country)
        conn.commit()
        
        # country id fetch from country table
        q=f'select SCOPE_IDENTITY();'
        countryid_value=cursor.execute(q).fetchone()[0]
        
        
        
        #City
        query_city=f"INSERT INTO City values('{row[10]}')"
        cursor.execute(query_city)
        
        # city id fetch from city table
        q=f'select SCOPE_IDENTITY();'
        cityid_value=cursor.execute(q).fetchone()[0]
        conn.commit() 
        
        
        #state
        query_state=f"INSERT INTO State values('{row[9]}')"
        cursor.execute(query_state)
        conn.commit()
        
        # state id fetch from state table
        q=f'select SCOPE_IDENTITY();'
        stateid_value=cursor.execute(q).fetchone()[0]
        
        
        #address 
        query3=f"""
                    INSERT INTO Address(Employee_ref_ID,country_id,state_id,city_id,street,Zipcode)
                    values({employeeid_value},
                    {countryid_value},{stateid_value},{cityid_value},'{(row[11])}','{row[12]}')
                    
                """
        cursor.execute(query3)
        conn.commit()
        
        
        # salary  
        query4=f"INSERT INTO Salary(EmployeeID,Salary) values({employeeid_value},{int(row[13])})"
        cursor.execute(query4)
        conn.commit()
        # # project  query 
        query5=f""" 
                    INSERT INTO Project(EmployeeID,DepartmentID,ProjectName,StartDate,EndDate,Budget,Status)
                    values({employeeid_value},
                    {department_value},'{row[17]}','{row[18]}','{row[19]}',\
                    {int(row[20])},'{row[21]}')
                    
                """

        cursor.execute(query5)
        conn.commit()
        
        
if __name__=='__main__':
    app.run(debug=True)
    
    