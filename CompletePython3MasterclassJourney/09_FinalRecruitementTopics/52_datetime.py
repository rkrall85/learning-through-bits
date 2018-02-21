import datetime

t = datetime.time(1,15,5) #hour, minute. sececonds

print(type(t))
print(t)
print(t.minute)

d = datetime.date(2018,10,11)
d2 = datetime.date.today()
print(d2)
d3 = datetime.datetime.now()
print(d3)

t0 = datetime.datetime.now()
result = [x**2 for x in range(10000)]
t1 = datetime.datetime.now()

diff = t1  - t0
print(diff.microseconds)
