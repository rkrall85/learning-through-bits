
#import db_connection as d
#crsr = d.database_connection()


class User():
    def __init__(self, db_connection,user_name, first_name= None, last_name=None, email=None):
        self.db_connection = db_connection
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    #getting the user profile from database.
    def GetUser(self):
        sql =  """\
                DECLARE	@user_id int,
		                  @first_name varchar(50),
		                  @last_name varchar(50),
		                  @email varchar(50),
		                  @message varchar(50);
                exec [dbo].[usp_GetUser] @user_name = ?,
                                             @user_id = @user_id OUTPUT,
                                             @first_name = @first_name OUTPUT,
                                             @last_name = @last_name OUTPUT,
                                             @email = @email OUTPUT,
                                             @message = @message OUTPUT;
                Select @user_id, @first_name, @last_name, @email, @message;
            """
        params = (self.user_name,) #creating parms
        self.db_connection.execute(sql, params) #executing sproc
        data = self.db_connection.fetchone() #putting results into row class
        user_id = data[0] #getting id
        first_name = data[1]
        last_name = data[2]
        email = data[3]
        message = data[4]
        return user_id,first_name, last_name, email, message
        #message = data[1] #getting message

    def CreateUser(self):
        sql = """\
                DECLARE	@user_id int, @message varchar(50);
                exec [dbo].[usp_CreateUser] @user_name = ?,
                                            @first_name = ?,
                                            @last_name = ?,
                                            @email = ?,
                                            @user_id = @user_id OUTPUT,
                                            @message = @message OUTPUT;
                Select @user_id, @message;
            """
        params = (self.user_name,self.first_name, self.last_name, self.email,) #creating parms
        self.db_connection.execute(sql, params) #executing sproc
        data = self.db_connection.fetchone() #putting results into row class
        user_id = data[0] #getting id
        message = data[1]
        return user_id,message
        #print('id', data.p_id)


#print(username.GetUser()[0])#output user_id
