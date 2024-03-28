from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
import db
from flask_jwt_extended import jwt_required
blp_project=Blueprint('project',__name__,description="operations on project")
@blp_project.route('/employee/project')
class Employee(MethodView):
    def __init__(self):
        self.db=db.Project()    
    
    @jwt_required(verify_type=False)
    def get(self):
        try:
            id=request.args.get('ProjectID')
            if id is None:
                return self.db.getAllProject()
            else:
                result=self.db.getParticularProject(id)
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
            self.db.addProject(request_data)
            return jsonify({"message":"project added successfully"}),201
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @jwt_required(verify_type=False)
    def put(self):
        try:
            projectID=request.args.get('ProjectID')
            request_data=request.get_json()
            if projectID is None:
                return jsonify({"message":"Please enter Projectid"})
            if self.db.updateProject(projectID,request_data):
                return jsonify({"message":"project update successfully"})
            else:
                return jsonify({"message":"data not found"}),404
        except Exception as e:
            return jsonify({'error': str(e)})
        
        
    @jwt_required(verify_type=False)   
    def delete(self):
        try:
            projectID=request.args.get('ProjectID')
            if id is None:
                return jsonify({"message":"Please enter projectID"})
            if self.db.deleteProject(projectID):
                return jsonify({"message":"data deleted"}),200
            else:
                return jsonify({"message":"data not found"}),404  
        except Exception as e:
            return jsonify({'error': str(e)})