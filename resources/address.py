from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
import db
from flask_jwt_extended import jwt_required
blp_address=Blueprint('employee address',__name__,description="operations on address")
@blp_address.route('/employee/address')
class Address(MethodView):
    def __init__(self):
        self.db=db.Address() 
           
    @jwt_required(verify_type=False)
    def get(self):
        
        try:
            id=request.args.get('AddressID')
            if id is None:
                return self.db.getAllEmployeeAddress()
            else:
                result=self.db.getParticularEmployeeAddress(id)
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
            self.db.addEmployeeAddress(request_data)
            return jsonify({"message":"data added successfully"}),201
        except Exception as e:
            return jsonify({'error': str(e)})
    
    @jwt_required(verify_type=False)    
    def put(self):
        
        try:
            addID=request.args.get('AddressID')
            request_data=request.get_json()
            if addID is None:
                return jsonify({"message":"Please enter Addressid"})
            if self.db.updateEmployeeAddress(addID,request_data):
                return jsonify({"message":"data update successfully"})
            else:
                return jsonify({"message":"data not found"}),404
            
        except Exception as e:
            return jsonify({'error': str(e)})
    
    @jwt_required(verify_type=False)   
    def delete(self):
        try:
            addid=request.args.get('AddressID')
            if addid is None:
                return jsonify({"message":"Please enter Addressid"})
            if self.db.deleteEmployeeAddress(addid):
                return jsonify({"message":"data deleted"}),200
            else:
                return jsonify({"message":"data not found"}),404
            
        except Exception as e:
            return jsonify({'error': str(e)})