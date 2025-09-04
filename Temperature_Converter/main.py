unit = input("Enter the unit of temperature C/F/K:") #Inputs the unit: Celsius, Fahrenheit, or Kelvin
temp = int(input("Enter the temperature in that unit:")) #Inputs the temperature in the same scale
unit = unit.lower() #Lowercases the unit input in order to simplify if condition

#Converts and prints Celsius into other scales
if unit == 'c':
	print(f"Fahrenheit: {1.8*temp +32}")
	print(f"Kelvin: {temp + 273.15}")

#Converts and prints Fahrenheit into other scales
elif unit == 'f':
	celsius = 5/9*(temp -32)
	print(f"Celsius: {celsius}")
	print(f"Kelvin: {celsius + 273.15}")

#Converts and prints Kelvin into other scales
elif unit == 'k':
	print(f"Fahrenheit: {(temp-273.15)*1.8+32}")
	print(f"Celsius: {temp - 273.15}")

else :
	print("Invalid")
