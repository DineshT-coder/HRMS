from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
import db
from flask_jwt_extended import jwt_required
blp_project=Blueprint('project',__name__,description="operations on project")
@blp_project.route('/employee/project')
class Project(MethodView):
    """
        The Project class is a Flask view class that handles HTTP requests related to employee information.
    """
    def __init__(self):
        """
            In the __init__ method, an instance of the EmployeeInformation class from the db module is
            created and stored in the self.db attribute
        """
        self.db=db.Project()    
    
    @jwt_required(verify_type=False)
    def get(self):
        """
            Handle post requests for project information
        """
        
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
        """
            Handle post requests for project information
        """
        
        request_data=request.get_json()
        try:
            self.db.addProject(request_data)
            return jsonify({"message":"project added successfully"}),201
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @jwt_required(verify_type=False)
    def put(self):
        """
            Handle put requests for project information
        """
        
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
        """
            Handle DELETE requests for project information
        """
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