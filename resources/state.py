from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
import db
from flask_jwt_extended import jwt_required
blp_state=Blueprint('employee state',__name__,description="operations on state")
@blp_state.route('/employee/state')
class State(MethodView):
    def __init__(self):
        self.db=db.State() 
           
    @jwt_required(verify_type=False)
    def get(self):
        try:
            id=request.args.get('state_id')
            if id is None:
                return self.db.getAllEmployeeState()
            else:
                result=self.db.getParticularEmployeeState()
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
            self.db.addEmployeeState(request_data)
            return jsonify({"message":"data added successfully"}),201
        except Exception as e:
            return jsonify({'error': str(e)})
    
    @jwt_required(verify_type=False)    
    def put(self):
        try:
            state_id=request.args.get('state_id')
            request_data=request.get_json()
            if state_id is None:
                return jsonify({"message":"Please enter state_id"})
            if self.db.updateEmployeeState(state_id,request_data):
                return jsonify({"message":"data update successfully"})
            else:
                return jsonify({"message":"data not found"}),404
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @jwt_required(verify_type=False)   
    def delete(self):
        try:
            state_id=request.args.get('state_id')
            if state_id is None:
                return jsonify({"message":"Please enter state_id"})
            if self.db.deleteEmployeeState(state_id):
                return jsonify({"message":"data deleted"}),200
            else:
                return jsonify({"message":"data not found"}),404
        except Exception as e:
            return jsonify({'error': str(e)})