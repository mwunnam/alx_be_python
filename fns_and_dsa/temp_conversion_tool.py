FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return result

def convert_to_fahrenheit(celsius):
    result = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return result


user_input = float(input("Enter the temperature to convert: "))
temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if isinstance(user_input, float):
    input_temp = user_input
else:
    print("Invalid temperature. Please enter a numeric value.")


if temp_unit == "C":
    temp = convert_to_fahrenheit(input_temp)
    print(f"{input_temp}{chr(176)}C is {temp}{chr(176)}F")
else:
    temp = convert_to_celsius(input_temp)
    print(f"{input_temp}{chr(176)}F is {temp}{chr(176)}C")
