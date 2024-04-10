from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
# from schemas import UserSchema,UserQuerySchema
import user_database
import hashlib
from flask import abort

from flask_jwt_extended import create_access_token,create_refresh_token
blp_user=Blueprint('Users',__name__,description="operations on users")

@blp_user.route('/login')
class Login(MethodView):
    """
        in this login class view class users that handles users login
    """
    def __init__(self):
        """
            this is constructor of this class that provides the access of user database from the user_database(python file)
        """
        self.db=user_database.Users()
    
    def post(self):
        """
            Handle post requests for users information and returns the access token and refresh token 
        """
        request_data=request.get_json()
        username=request_data['username']
        password=request_data['password']
        hashed_password=hashlib.sha256(password.encode('utf-8')).hexdigest()
    
        result=self.db.verify_user(username,hashed_password)
        if result:
            return jsonify({"access_token":create_access_token(identity=result['id']),
                            'refresh_token':create_refresh_token(identity=result['id'])})
        abort(400,{"message":"Username or Password is Incorrect"})       



@blp_user.route('/user')
class User(MethodView):
    """
        this class is use for to insert a new users into the database and handle users related request
    """
    def __init__(self):
        """
            this is constructor of this class that provides the access of user database from the user_database(python file)
        """
        self.db=user_database.Users()
     
    def get(self):
        """
            Handle get requests for users information
        """
        id=int(request.args.get('id'))
        result=self.db.get_user(id)
        if result is None:
            return jsonify({"message":"User doesn't exist"}),404
        else:
            return result 
    

    def post(self):
        """
            Handle post requests for users information
        """
        request_data=request.get_json()
        username=request_data['username']
        password=request_data['password']
        hashed_password=hashlib.sha256(password.encode('utf-8')).hexdigest()
        if 'username' not in request_data or 'password' not in request_data:
            return jsonify({"message":"Insert all fields"})
        else:
            self.db.add_user(username,hashed_password)
            return jsonify({"message":"user added successfully"}),201
        
    def delete(self):
        """
            Handle delete requests for users information
        """
        id=int(request.args.get('id'))
        if id is None:
            return jsonify({"message":"Please enter id"})
        if self.db.delete_user(id):
            return jsonify({"message":"user deleted"}),200
        else:
            return jsonify({"message":"user not found"}),404