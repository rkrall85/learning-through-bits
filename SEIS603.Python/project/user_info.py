
import db_connection as d
crsr = d.database_connection()


class User():
    def __init__(self, user_name, first_name= None, last_name=None, email=None):
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
        crsr.execute(sql, params) #executing sproc
        data = crsr.fetchone() #putting results into row class
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
        crsr.execute(sql, params) #executing sproc
        data = crsr.fetchone() #putting results into row class
        user_id = data[0] #getting id
        message = data[1]
        return user_id,message
        #print('id', data.p_id)


#def main():
current_user = str(input("Are you a user(y/n)?"))
if current_user.lower() == 'y':
    user_name = str(input("Please enter your user name:"))
    if user_name is None: user_name = 'robert.krall' #just for testing so I can dont have ot run script from terminal to get input.
    user_profile = User(user_name)
    #if user_profile.GetUser()[0] != 0:
    print("Welcome back {}!".format(user_profile.GetUser()[1]))
else:
    print("Please answer the following questions to set up an account")
    user_name   = input("User Name:")
    first_name  = input("First Name:")
    last_name   = input("Last Name:")
    email       = input("email:")
    user_profile = User(user_name,first_name,last_name, email)
    if user_profile.CreateUser()[0] != 0:
        print("You have successful created an account. Your user id is {}!".format(user_profile.GetUser()[0]))




#print(username.GetUser()[0])#output user_id

'''
if username.GetUser() == 0:
    Print("sorry no user")
else:
    print("found user")
'''


'''
if user.CheckUser == 0:
    #InsertPerson()
    print(p_id)
'''
