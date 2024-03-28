from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
import db
from flask_jwt_extended import jwt_required
blp_city=Blueprint('employee city',__name__,description="operations on city")
@blp_city.route('/employee/city')
class State(MethodView):
    def __init__(self):
        self.db=db.City() 
           
    @jwt_required(verify_type=False)
    def get(self):
        
        try:
            id=request.args.get('city_id')
            if id is None:
                return self.db.getAllEmployeeCity()
            else:
                result=self.db.getParticularEmployeeCity()
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
            self.db.addEmployeeCity(request_data)
            return jsonify({"message":"data added successfully"}),201
        except Exception as e:
            return jsonify({'error': str(e)})
    
    @jwt_required(verify_type=False)    
    def put(self):
        try:
            city_id=request.args.get('city_id')
            request_data=request.get_json()
            if city_id is None:
                return jsonify({"message":"Please enter city_id"})
            if self.db.updateEmployeeCity(city_id,request_data):
                return jsonify({"message":"data update successfully"})
            else:
                return jsonify({"message":"data not found"}),404
        except Exception as e:
            return jsonify({'error': str(e)})
        
        
    @jwt_required(verify_type=False)   
    def delete(self):
        try:
            city_id=request.args.get('city_id')
            if city_id is None:
                return jsonify({"message":"Please enter city_id"})
            if self.db.deleteEmployeeCity(city_id):
                return jsonify({"message":"data deleted"}),200
            else:
                return jsonify({"message":"data not found"}),404    
        except Exception as e:
            return jsonify({'error': str(e)})