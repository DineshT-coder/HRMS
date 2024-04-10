from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
import db
from flask_jwt_extended import jwt_required


blp_employeeNthSalary=Blueprint('employeeNthSalary',__name__,description="operations on employee")

@blp_employeeNthSalary.route('/employee/nthSalary')
class EmployeeNthSalary(MethodView):
    """
        The EmployeeNthSalary class is a Flask view class that handles HTTP requests related to employee information.
    """
    def __init__(self):
        """
            In the __init__ method, an instance of the EmployeeInformation class from the db module is
            created and stored in the self.db attribute
        """
        self.db=db.EmployeeNthSalary() 
        
    @jwt_required(verify_type=False)
    def get(self):
        """
            Handle get requests for salary information
        """
        try:
            rank=int(request.args.get('Rank'))
            if rank is not None:
                return self.db.getAllEmployeeRecord(rank),200
        except Exception as e:
            return jsonify({'error': str(e)})    
