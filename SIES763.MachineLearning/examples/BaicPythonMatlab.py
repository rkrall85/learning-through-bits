
# coding: utf-8

# In[ ]:


# basic array
import numpy as np
a =np.array( [ (1, 2, 3), (7, 8, 9) ] )     # Matlab a = [1 2 3; 7 8 9]
print(a)
print('Transpose of array a = ')
print(np.transpose(a))                   # Matlab a'


# In[ ]:


# basic info about an array
print('size = ', a.size)                    # Matlab size(a)
print('shape = ', a.shape)                  # Matlab size(a)
print('a.max() = ', a.max())                # Matlab max(a(:))
print('a.min() = ', a.min())
print('a.mean() = ', a.mean())
print('a.mean(axis) = ', a.mean(axis=0))


# In[ ]:


# ones or zeros
b = np.ones( (2,3) ) * 2 + 4             # Matlab b = ones(2, 3) * 2 + 4
print(b)
print('size = ', b.size)                 # Matlab size(b)
print('b.sum = ', b.sum())               # Matlab sum(b(:))
print('b.sum(axis) = ', b.sum(axis=1))   # Matlab sum(b)


# In[ ]:


# simple operations, same as in Matlab
a=a+1
print(a)
print(a+b)     # print(a*b)


# In[ ]:


# random numbers
c = np.random.random( (2,3) ) * 2 + 4    # Matlab c = rand(2, 3)
print(c)


# In[ ]:


# colon operator ":"
print(a)
print('Get all rows and some columns = ')
print(a[:, 1:3])                          # Matlab a(:, 2:3)
print('Get row x and all columns = ')
print(a[1, :])                            # Matlab a(2, :)
# colon operator, everything
print('Reset all elements in c to 0')
c[:] = 0                                  # Matlab c = 0 
print(c)


# In[ ]:


# more colon operator ":"
d = np.arange(15)       # Matlab d =[1:15]
print('arange(x) = ')
print(d)
d = np.arange(1, 15, 5)    # Matlab d = [1:5:15]
print('arange(x1, x2, gap) = ')
print(d)
d = np.arange(0, 2, 0.5)   # Matlab d = [0 : 0.5 : 2]
print('arange(x1, x2, gap) = ')
print(d)


# In[ ]:


# concat E = [a, a]   or E = [a; a]
E = np.concatenate((a, b))           # Matlab E = [a; b]
print('concat vertically = ')
print(E)
E = np.concatenate((a, b), axis=1)   # Matlab E = [a b]
print('concat horizontally = ')
print(E)


# In[ ]:


''' 
find / search (R > 5)
and lots of comments
'''
R = np.random.random( (3,4) ) * 10 + 1    # Matlab R = rand(3, 4) * 10 + 1
print('Original randome array R = ')
print(R)
idx = np.where(R >= 10)
print('idx = ', idx)
print('idx[0] = ', idx[0])
print('idx[1] = ', idx[1])


# In[ ]:


# for loop
print('loop rang(3) = ')           # Matlab for i = 0 : 2
for i in range(3):
    print(i)
print('loop rang(0, 10, 2) = ')    # Matlab for i = 0 : 2 : 10 (or 8)
for i in range(0, 10, 2):
    print(i)
print('floating point loop = ')    # Matlab for i = 0 : 0.5 : 2 (or 1.5)    
float_loop = np.arange(0, 2, 0.5)
for i in float_loop:
    print(i)
    #time.sleep(0.5)


# In[ ]:


# reshape
print('Original array a = ')
print(a)
print('Reshape array a = ')
print(a.reshape(1, a.size))

