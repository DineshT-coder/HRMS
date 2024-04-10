from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
import db
from flask_jwt_extended import jwt_required
blp_salary=Blueprint('employee salary',__name__,description="operations on salary")
@blp_salary.route('/employee/salary')
class Salary(MethodView):
    """
        The salary class is a Flask view class that handles HTTP requests related to employee information.
    """
    def __init__(self):
        """
            In the __init__ method, an instance of the EmployeeInformation class from the db module is
            created and stored in the self.db attribute
        """
        self.db=db.Salary()    
    
    @jwt_required(verify_type=False)
    def get(self):
        """
            Handle get requests for salary information
        """
        try:
            id=request.args.get('SalaryID')
            if id is None:
                return self.db.getAllEmployeeSalary()
            else:
                result=self.db.getParticularEmployeeSalary(id)
                if result is None:
                    return jsonify({"message":"Record doesn't exist"}),404
                else:
                    return result
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @jwt_required(verify_type=False)        
    def post(self):
        """
            Handle post requests for salary information
        """
        request_data=request.get_json()
        try:
            self.db.addEmployeeSalary(request_data)
            return jsonify({"message":"data added successfully"}),201
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @jwt_required(verify_type=False)    
    def put(self):
        """
            Handle put requests for salary information
        """
        try:
            salaryID=request.args.get('SalaryID')
            request_data=request.get_json()
            if salaryID is None:
                return jsonify({"message":"Please enter Salaryid"})
            if self.db.updateEmployeeSalary(salaryID,request_data):
                return jsonify({"message":"data update successfully"})
            else:
                return jsonify({"message":"data not found"}),404
        except Exception as e:
            return jsonify({'error': str(e)})
     
    @jwt_required(verify_type=False)   
    def delete(self):
        """
            Handle delete requests for salary information
        """
        try:
            salid=request.args.get('SalaryID')
            if salid is None:
                return jsonify({"message":"Please enter Salaryid"})
            if self.db.deleteEmployeeSalary(salid):
                return jsonify({"message":"data deleted"}),200
            else:
                return jsonify({"message":"data not found"}),404
        except Exception as e:
            return jsonify({'error': str(e)})