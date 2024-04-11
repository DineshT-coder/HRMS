from flask import request,jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
import db
from flask_jwt_extended import jwt_required
from bulk_upload_functions import bulk

blp_manager=Blueprint('manager',__name__,description="operations on employee of manager")
@blp_manager.route('/employee/manager')
class Manager(MethodView):
    """
        The Employee class is a Flask view class that handles HTTP requests related to employee information.
    """
    def __init__(self):
        """
            In the __init__ method, an instance of the EmployeeInformation class from the db module is
            created and stored in the self.db attribute
        """
        self.db=db.EmployeeInformation()
        
        self.obj=db.DataBaseConnectivity()  
          
        
    @jwt_required(verify_type=False)       
    def post(self):
        """
            Handle POST requests for manager information
        """
        try:    
            request_data=request.get_json()
            employee_id=request_data['EmployeeID']
            manager_id=request_data['ManagerID']
            
            query=f"SELECT * FROM Employee WHERE EmployeeID ={employee_id}"
            self.obj.cursor.execute(query)
            result=self.obj.cursor.fetchone()
            print(result)
            if result is None:
                return jsonify({'error': f'Employee ID {employee_id} does not exist'}), 404
            
            else:
                
                query=f"Select count(*) from employee where employeeid={manager_id}"
                self.obj.cursor.execute(query)
                result=self.obj.cursor.fetchone()[0]
                
                if result!=0:
                    query=f"UPDATE Employee SET  ManagerID={manager_id} where EmployeeID={employee_id}"
                    result=self.obj.cursor.execute(query)
                    self.obj.conn.commit()
                    return jsonify({'message': f'Manager with employee id update'})
                
                else:
                    return jsonify({'message':"Manager with employee id does not exist"}),404
                
        except Exception as e:
            return jsonify({'error': str(e)}),400

