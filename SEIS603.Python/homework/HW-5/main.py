
#Robert Krall
#SEIS603 - homework 5


print("Please enter a list of words or numbers")
#getting a list of strings or numbers from user
input_list = eval(input("input list:"))
#create an empty list for creating a distinct list of words/numbers entered
distinct_list = []
#loop through all the entries in list and put distinct values in a new list
#also convert everything to string
for l in range(len(input_list)):
    if input_list[l] not in distinct_list:
        distinct_list.append(str(input_list[l]))

#sorting the distinct list
distinct_list.sort()

#outputting the distinct list
print("The distinct ordered list you entered")
print(distinct_list)
