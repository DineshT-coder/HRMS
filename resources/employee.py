from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
import db
from flask_jwt_extended import jwt_required
blp=Blueprint('employee',__name__,description="operations on employee")
@blp.route('/employee')
class Employee(MethodView):
    def __init__(self):
        self.db=db.EmployeeInformation()  
           

    @jwt_required(verify_type=False)
    def get(self):
        try:
            id=request.args.get('EmployeeID')
            if id is None:
                return jsonify(self.db.getAllEmployeeRecord())
            else:
                result=self.db.getParticularEmployeeRecord(id)
                if result is None:
                    return jsonify({"message":"Record doesn't exist"}),404
                else:
                    return result
        except Exception as e:
            return jsonify({'error': str(e)})
        
        
    @jwt_required(verify_type=False)       
    def post(self):
        try:    
            request_data=request.get_json()
            self.db.addEmployeeRecord(request_data)
            return jsonify({"message":"Employee data added successfully"}),201
        
        except Exception as e:
            return jsonify({'error': str(e)})

    @jwt_required(verify_type=False)   
    def put(self):
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
    def delete(self):
        
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