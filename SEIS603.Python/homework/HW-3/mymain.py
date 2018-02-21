#Robert Krall
#mymain.py


#from temperatureConverter import celsiusToFahrenheit, fahrenheitToCelsius
import temperatureConverter as tc

print("*"*100)

user_fahrenheit = int(input("What is the fahrenheit degree?"))
c = tc.fahrenheitToCelsius(user_fahrenheit)
print(str(user_fahrenheit) + " degrees fahrenheit converts to " + str(c) + " degrees celsius")

print("*"*100)

user_celsius  = int(input("What is the celsius temperature degree?"))
f = tc.celsiusToFahrenheit(user_celsius)
print(str(user_celsius) + " degrees celsius converts to " + str(f) + " degrees fahrenheit")

print("*"*100)
