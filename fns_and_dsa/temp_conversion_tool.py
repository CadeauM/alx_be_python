# this file defines functions to convert temperatures between Celsius and Fahrenheit
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    
def main():
    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if unit == 'C':
        converted_to_fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_to_fahrenheit}°F")
    elif unit == 'F':
        converted_to_celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_to_celsius}°C")
    else:
        print('Invalid temperature. Please enter a numeric value.')
        
if __name__ == "__main__":
    main()
