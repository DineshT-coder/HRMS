from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
import db
from flask_jwt_extended import jwt_required


blp_employeeNthSalary=Blueprint('employeeNthSalary',__name__,description="operations on employee")

@blp_employeeNthSalary.route('/employee/nthSalary')
class EmployeeNthSalary(MethodView):
    def __init__(self):
        self.db=db.EmployeeNthSalary() 
        
    @jwt_required(verify_type=False)
    def get(self):
        try:
            rank=int(request.args.get('Rank'))
            if rank is not None:
                return self.db.getAllEmployeeRecord(rank)
        except Exception as e:
            return jsonify({'error': str(e)})    
