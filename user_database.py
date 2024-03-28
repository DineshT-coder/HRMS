import db
class Users(db.DataBaseConnectivity):
    
    def get_user(self,id):
        query=f"Select * From Users where id={id}"
        self.cursor.execute(query)
        result=self.cursor.fetchone()
        user_dict={}
        if result is not None:
            user_dict['id']=result[0]
            user_dict['username']=result[1]
            return user_dict
            
    def add_user(self,username,password):
        query=f"INSERT INTO Users values('{username}','{password}')"
        self.cursor.execute(query)
        self.conn.commit()
    
    def delete_user(self,id):
        query=f"Delete from Users where id={id}"
        self.cursor.execute(query)
        if self.cursor.rowcount!=0:
            self.conn.commit()
            return True
        else:
            return False
        
    def verify_user(self,username,password):
        query=f"Select * from users Where username='{username}' AND password='{password}'"
        self.cursor.execute(query)
        result=self.cursor.fetchone()
        user_dict={}
        if result is not None:
            user_dict['id']=result[0]
            return user_dict