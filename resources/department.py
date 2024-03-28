from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
import db
from flask_jwt_extended import jwt_required
blp_department=Blueprint('employee department',__name__,description="operations on department")
@blp_department.route('/employee/department')
class Department(MethodView):
    def __init__(self):
        self.db=db.Department()    
    
    @jwt_required(verify_type=False)
    def get(self):
        try:
            id=request.args.get('DepartmentID')
            if id is None:
                return self.db.getAllEmployeeDepartment()
            else:
                result=self.db.getParticularEmployeeDepartment(id)
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
            self.db.addEmployeedepartment(request_data)
            return jsonify({"message":"data added successfully"}),201
    
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @jwt_required(verify_type=False)    
    def put(self):
        
        try:
            depID=request.args.get('DepartmentID')
            request_data=request.get_json()
            if depID is None:
                return jsonify({"message":"Please enter DepartmentID"})
            if self.db.updateEmployeeDepartment(depID,request_data):
                return jsonify({"message":"data update successfully"})
            else:
                return jsonify({"message":"data not found"}),404
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @jwt_required(verify_type=False)
    def delete(self):
        try:
            depid=request.args.get('DepartmentID')
            if depid is None:
                return jsonify({"message":"Please enter DepartmentID"})
            if self.db.deleteEmployeeDepartment(depid):
                return jsonify({"message":"data deleted"}),200
            else:
                return jsonify({"message":"data not found"}),404
            
        except Exception as e:
            return jsonify({'error': str(e)})