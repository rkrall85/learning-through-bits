#main program to handle input from user.

import db_connection as d

connection = d.database_connection()

current_user = input("Are you a current user?:")
if current_user.lower() == 'y':
    user_name = input("Please enter your user name:")


    SQLCommand = "SELECT p.p_id, p.f_name FROM dbo.Person AS p WHERE p.u_name = ?"
    Values = [user_name.lower()]
    connection.execute(SQLCommand,Values)
    results = connection.fetchone()
    print("hello " + results[1] + " (" + str(results[0]) + ")")


else:
    print("Please answer the following questions to set up an account")
    first_name  = input("First Name:")
    last_name   = input("Last Name:")
    user_name   = input("User Name:")
    email       = input("email:")

    SQLCommand = ("INSERT INTO Person (f_name, l_name, u_name, email) "
                                "VALUES (?,?,?,?)")
    Values = [first_name,last_name,user_name.lower(),email]

    connection.execute(SQLCommand,Values)
    connection.commit()

connection.close()
