#Robert Krall
#SEIS603 - Python File

#files we are working with
infile  = open('input.txt', 'r')  #read mode
outfile = open('output.txt', 'w')   # write mode
aline = infile.readline()#variable to read the lines in file

while aline:
    #put row into list
    values = aline.split('-')
    #variables
    last_name       = values[0]
    first_name      = values[1]
    score           = int(values[2]) #cast to int to so we can do calc
    total_points    = int(values[3][:-1]) #cast to int so we can do calc
    percentage      = (score/total_points)*100 #calc the grade percentage
    #figuing out the letter grade
    if percentage > 90:                             grade = 'A'
    elif percentage >= 80 and percentage <= 89:     grade = 'B'
    elif percentage >= 70 and percentage <= 79:     grade = 'C'
    else:                                           grade = 'F'

    new_values = last_name + '-' \
                + first_name + '-' \
                + str(score) + '-' \
                + str(total_points) + '-' \
                + grade +'\n'
    #print(new_values)
    outfile.write(new_values) #output row into new file
    aline = infile.readline() #grab new line

#make sure to close both files
infile.close()
outfile.close()
