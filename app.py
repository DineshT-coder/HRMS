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
from resources.manager import blp_manager
from flask_jwt_extended import JWTManager
import pyodbc
import os
import pandas as pd
from headersfile.common_header import blp_header

from  bulk_upload_functions import bulk

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
api.register_blueprint(blp_manager)
api.register_blueprint(blp_header)

app.config['DEBUG']=True
UPLOAD_FOLDER='uploads'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER 

try:
    conn=pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-KGD64VN9;DATABASE=employeeinformation;')
    cursor=conn.cursor()
except Exception as e:
    print({'error': str(e)})
@app.route('/employee/csvdata')  
def home():
    """
        this function is flask view function responsible for rendering template
    """
    
    return render_template('index.html')

@app.route('/employee/csvdata',methods=['POST'])
def upload_files():
    """
        this function is responsible for handling upload csv file
    """
    upload_file=request.files['file']
    if upload_file.filename !='':   
        file_path=os.path.join(app.config['UPLOAD_FOLDER'],upload_file.filename)
        upload_file.save(file_path)
        parseCsv(file_path)
        return "upload successfully"
    else:
        return "file not upload"

def parseCsv(file_path):
    """
        parcsv function reads a csv file and process each row
    """
    
    csvData=pd.read_csv(file_path)
    for i,row in csvData.iterrows():
        if  bulk.is_employee_exists(cursor,row) == 0 :
            department_id=bulk.get_or_insert_Department(cursor,conn,row['Department Name'])
            bulk.insert_employee(cursor,conn,row, department_id)
            employee_id = bulk.get_employee_id(cursor,row['FirstName'],row['PhoneNumber'],row['Email']) 
            bulk.insert_address(cursor,conn,row, employee_id)
            bulk.insert_salary(cursor,conn,row,employee_id)
            bulk.insert_qualification(cursor,conn,row,employee_id)
            bulk.insert_project(cursor,conn,row,employee_id,department_id)
        else:
            pass
    
if __name__=='__main__':
    app.run(debug=True)
    
        

     
        
    