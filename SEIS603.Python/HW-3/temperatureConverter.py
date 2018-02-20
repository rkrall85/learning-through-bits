#Robert Krall
#temperatureConverter.py
#Fahrenheit = 9/5 * Celsius + 32

def fahrenheitToCelsius(tempInFahrenheit):
    '''
    input: temperature in fahrenheit
    output: temperature in Celsius
    summary: function will convert temperature from F to C
    '''
    return round(((tempInFahrenheit - 32)/ (9/5)),2)

def celsiusToFahrenheit(tempInCelsius) :
    '''
    input: temperature in Celsius
    output: temperature in fahrenheit
    summary: function will convert temperature from C to F
    '''
    return round((9/5 * tempInCelsius + 32),2)
