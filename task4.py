def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

prompt=("Enter temperature in Celsius: ")
celsius = float(input(prompt))   
fahrenheit = celsius_to_fahrenheit(celsius)
print("Temperature in Fahrenheit:", fahrenheit)
