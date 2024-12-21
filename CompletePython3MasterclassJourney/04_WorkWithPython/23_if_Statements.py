

if 1>2:
    print("condition met")

cond = 1< 2
if cond:
    print("cond met")


if 1==10:
    print("condition met 1==1")
else:
    print("Last block happened to run")

if 2 == 0:
    print('first condition true')
elif 2 == 1:
    print("second condition true")
elif 2 == 2:
    print("Third condition true")
else:
    print("nothing above was true")

#########################
agent_code = 2311912
access = False
if agent_code == 12345:
    print("code reset")
    print("call a supervisor")
elif agent_code == 2311912:
    print("Welcome agent 2311912")
    access = True
else:
    print("Sorry no matching code")

####################
if access == True: #you can write as If access: 
    print("Access Granted")
else:
    print("Access Denied")
