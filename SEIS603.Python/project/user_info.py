
#import db_connection as d
#crsr = d.database_connection()

import sys

class User():
    def __init__(self, db_connection,current_user):
        self.db_connection  = db_connection
        self.current_user   = current_user


    #will either look up for create a new one
    def UserProfile(db_connection):
        if self.current_user.lower() == 'y':
            user_name = str(input("Please enter your user name:"))
            if user_name.lower() == 'exit':
                sys.exit()
            else:
                u_id    = self.GetUser(user_name)[0]
                f_name  = self.GetUser(user_name)[1]
                l_name  = self.GetUser(user_name)[2]
                email   = self.GetUser(user_name)[3],
                if u_id == 0:
                    print("Your ID was not found. Please try again or enter exit")
                    self.UserProfile()
                else:
                    print("Welcoem Back {}".format(f_name))
                    return u_id, f_name, l_name, email
        else:
            print("Please answer the following questions to set up an new account")
            user_name   = input("User Name:")
            first_name  = input("First Name:")
            last_name   = input("Last Name:")
            email       = input("Email:")
            u_id        = self.CreateUser(user_name,first_name,last_name,email)[0]
            if u_id == 0:
                print("Error happend. Please try again or enter exit")
                self.UserProfile()
            else:
                print("Thank you for creating a profile {}".format(f_name))
                return u_id, first_name, last_name, email

    #getting the user profile from database.
    def GetUser(self, u_name):
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
        params = (u_name,) #creating parms
        self.db_connection.execute(sql, params) #executing sproc
        data = self.db_connection.fetchone() #putting results into row class
        user_id = data[0] #getting id
        first_name = data[1]
        last_name = data[2]
        email = data[3]
        message = data[4]
        self.db_connection.commit()#need this to commit transaction
        return user_id,first_name, last_name, email, message
        #message = data[1] #getting message

    def CreateUser(self, u_name, f_name, l_name, email):
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
        params = (u_name,f_name, l_name, email,) #creating parms
        self.db_connection.execute(sql, params) #executing sproc
        data = self.db_connection.fetchone() #putting results into row class
        user_id = data[0] #getting id
        message = data[1]
        self.db_connection.commit()#need this to commit transaction
        return user_id,message
        #print('id', data.p_id)


#print(username.GetUser()[0])#output user_id
