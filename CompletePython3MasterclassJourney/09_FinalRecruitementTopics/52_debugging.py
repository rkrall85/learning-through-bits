import  pdb #pythong debuggger


#debugging

x = '1'
y = 2
z = 3


result = y + z
print(result)

#enable trace
pdb.set_trace() #run through termianl or jupyter

new_result   = y + x
print(new_result)
