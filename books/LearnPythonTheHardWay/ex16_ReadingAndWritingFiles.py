






# Commands to remember
'''
close -- Closes the file. Like File->Save.. in your editor.
read -- Reads the contents of the file, you can assign the result to a variable.
readline -- Reads just one line of a text file.
truncate -- Empties the file, watch out if you care about the file.
write(stuff) -- Writes stuff to the file.
'''


from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that hit Ctrl-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file....")
target = open(filename, 'w')

print("truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")

'''
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
'''
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print("And Finally , we close it.")
target.close()
