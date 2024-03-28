from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
import db
from flask_jwt_extended import jwt_required
blp_qualification=Blueprint('employee qualification',__name__,description="operations on qualification")
@blp_qualification.route('/employee/qualification')
class Qualification(MethodView):
    def __init__(self):
        self.db=db.Qualification()    
    
    @jwt_required(verify_type=False)
    def get(self):
        try:
            id=request.args.get('QualificationID')
            if id is None:
                return self.db.getAllEmployeeQualification()
            else:
                result=self.db.getParticularEmployeeQualification(id)
                if result is None:
                    return jsonify({"message":"Record doesn't exist"}),404
                else:
                    return result
        except Exception as e:
            return jsonify({'error': str(e)})
                
    @jwt_required(verify_type=False)        
    def post(self):
        request_data=request.get_json()
        try:
            self.db.addEmployeeQualification(request_data)
            return jsonify({"message":"data added successfully"}),201
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @jwt_required(verify_type=False)   
    def put(self):
        try:
            ID=request.args.get('QualificationID')
            request_data=request.get_json()
            if ID is None:
                return jsonify({"message":"Please enter qualificationID"})
            if self.db.updateEmployeeQualification(ID,request_data):
                return jsonify({"message":"data update successfully"})
            else:
                return jsonify({"message":"data not found"}),404
        except Exception as e:
            return jsonify({'error': str(e)})
        
        
    @jwt_required(verify_type=False)   
    def delete(self):
        try:
            id=request.args.get('QualificationID')
            if id is None:
                return jsonify({"message":"Please enter QualificationID"})
            if self.db.deleteEmployeeQualification(id):
                return jsonify({"message":"data deleted"}),200
            else:
                return jsonify({"message":"data not found"}),404
        except Exception as e:
            return jsonify({'error': str(e)})