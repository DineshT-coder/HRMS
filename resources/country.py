from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
import db
from flask_jwt_extended import jwt_required
blp_country=Blueprint('employee country',__name__,description="operations on country")
@blp_country.route('/employee/country')
class Country(MethodView):
    def __init__(self):
        self.db=db.Country() 
           
    @jwt_required(verify_type=False)
    def get(self):
        try:
            id=request.args.get('country_id')
            if id is None:
                return self.db.getAllEmployeeCountry()
            else:
                result=self.db.getParticularEmployeeCountry()
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
            self.db.addEmployeeCountry(request_data)
            return jsonify({"message":"data added successfully"}),201
        except Exception as e:
            return jsonify({'error': str(e)})
    
    @jwt_required(verify_type=False)    
    def put(self):
        try:
            country_id=request.args.get('country_id')
            request_data=request.get_json()
            if country_id is None:
                return jsonify({"message":"Please enter country_id"})
            if self.db.updateEmployeeCountry(country_id,request_data):
                return jsonify({"message":"data update successfully"})
            else:
                return jsonify({"message":"data not found"}),404
        except Exception as e:
            return jsonify({'error': str(e)})
        
        
    @jwt_required(verify_type=False)   
    def delete(self):
        try:
            country_id=request.args.get('country_id')
            if country_id is None:
                return jsonify({"message":"Please enter country_id"})
            if self.db.deleteEmployeeCountry(country_id):
                return jsonify({"message":"data deleted"}),200
            else:
                return jsonify({"message":"data not found"}),404
        except Exception as e:
            return jsonify({'error': str(e)})