from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
import db
from flask_jwt_extended import jwt_required
from bulk_upload_functions import bulk


blp=Blueprint('employee',__name__,description="operations on employee")
@blp.route('/employee')
class Employee(MethodView):
    """
        The Employee class is a Flask view class that handles HTTP requests related to employee information.
    """
    def __init__(self):
        """
            In the __init__ method, an instance of the EmployeeInformation class from the db module is
            created and stored in the self.db attribute
        """
        self.db=db.EmployeeInformation()
        
        self.obj=db.DataBaseConnectivity()  
           

    @jwt_required(verify_type=False)
    def get(self):
        """
            Handle GET requests for employee information
        """
        try:
            id=request.args.get('EmployeeID')
            if id is None:
                return jsonify(self.db.getAllEmployeeRecord()),200
            else:
                result=self.db.getParticularEmployeeRecord(id),200
                if result is None:
                    return jsonify({"message":"Record doesn't exist"}),404
                else:
                    return result
        except Exception as e:
            return jsonify({'error': str(e)})
        
        
    @jwt_required(verify_type=False)       
    def post(self):
        """
            Handle POST requests for employee information
        """
        try:    
            request_data=request.get_json()
            print(request_data)
            if bulk.is_employee_exists(self.obj.cursor,request_data)==0:
                employee_id=self.db.addEmployeeRecord(request_data)
                return jsonify({"message":"Employee data added successfully",
                                "EmployeeID":int(employee_id)}),201
            else:
                return jsonify({"message":"Employee is already exist in the database,duplicate data not allowed"})
        
        except Exception as e:
            return jsonify({'error': str(e)})

    @jwt_required(verify_type=False)   
    def put(self):
        """
            Handle PUT requests for employee information
        """
        try:
            empID=request.args.get('EmployeeID')
            request_data=request.get_json()
            if empID is None:
                return jsonify({"message":"Please enter employeeid"})
            if self.db.updateEmployeeRecord(empID,request_data):
                return jsonify({"message":"data update successfully"})
            else:
                return jsonify({"message":"data not found"}),404
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @jwt_required(verify_type=False)   
    def patch(self):
        """
            Handle PATCH requests for employee information
        """
        try:
            empID=request.args.get('EmployeeID')
            request_data=request.get_json()
            if empID is None:
                return jsonify({"message":"Please enter employeeid in the parameter"})
            if self.db.employee_patch_method(empID,request_data):
                return jsonify({"message":"data update successfully"})
            else:
                return jsonify({"message":"data not found"}),404
        except Exception as e:
            return jsonify({'error': str(e)})
    
    @jwt_required(verify_type=False) 
    def delete(self):
        """
            Handle DELETE requests for employee information
        """
        try:
            empid=request.args.get('EmployeeID')
            if id is None:
                return jsonify({"message":"Please enter employeeid"})
            if self.db.deleteEmployeeRecord(empid):
                return jsonify({"message":"data deleted"}),200
            else:
                return jsonify({"message":"data not found"}),404
            
        except Exception as e:
            return jsonify({'error': str(e)})