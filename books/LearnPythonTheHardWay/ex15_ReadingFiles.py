


from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read()) #output file contents


print ("I'll also ask you to type it again:" )
file_again = input("> ")

txt_again = open(file_again)

print (txt_again.read())
