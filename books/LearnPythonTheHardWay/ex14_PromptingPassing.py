


from sys import argv

script, user_name = argv #takes arguments from when you call the script
prompt = '> '

print ("Hi %s, I'm the %s script" % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
city = input(prompt)

print("What kind of comptuer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r.
But I can't feel it because I'm a robot.
And you have a %r computer. Nice.
"""% (likes, city, computer))
