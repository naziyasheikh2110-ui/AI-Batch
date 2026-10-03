# que 1 Write a program that asks the user for their name and age, then prints a sentence

# username = input("Enter your name: ")
# age = input("Enter your age: ")

# print("Hello" , username, ", you are" , age, "years old.")

# --------------------------------------------------------------

#que 2 Take two numbers as input from the user and print their sum,difference,product,and quotient

# a = float(input("Enter 1st number: "))
# b = float(input("Enter 2nd number: "))

# print("Sum: ", a+b)
# print("Difference: ", a-b)
# print("Product: ", a*b)
# print("Quotient: ", a/b)

# --------------------------------------------------------------

#que 3 Ask the user to enter two integers and one float. Convert them all to floats and print their average.

# a = int(input("Enter an integer: "))
# b = int(input("Enter another integer: "))
# c = float(input("Enter a float: "))

# avg = float(a+b+c)/3

# print("The average of these 3 numbers is: " , avg)

# --------------------------------------------------------------

#que 4 The user enters a string containing a number (e.g., "45"). Convert it to: Q4 "45" • an integer • a float • a string again Print all three values with their types

# num_str = input("Enter a String containing a number: ")

# num_int = int(num_str)
# num_float = int(num_str)

# print(num_int, type(num_int))
# print(float, type(num_float))
# print(num_str, type(num_str))

# --------------------------------------------------------------

#que 5 Evaluate and print the result of the following expression
# x = 10 + 3 * 2 **2  #10 + 3 * 4 -> 10 + 12 -> 22
# print(x)

# --------------------------------------------------------------

# que 6 Write a program to swap values of two numbers entered by the user.

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# c = a
# a = b 
# b = c 

# print("Swapped value of a: " , a)
# print("Swapped value of b: " , b)

# --------------------------------------------------------------

# que 7 celsius into fahrenheit 
# celsius_temp = float(input("Enter the temp in Celsius "))

# fahrenheit_temp = (celsius_temp * (9/5)) + 32

# print("Celsius Temprature " , celsius_temp , "°C in Fahrenheit is = " , fahrenheit_temp, "°F")

# ----------------------------------------------------------------

# Que 8 Take the radius (r) as user input and print the area.

# r =  float(input("Enter the radius (r): "))
# PI = 3.14

# area = PI * r * r

# print("Area = " , area)

# --------------------------------------------------------------------

# Que 9 Ask the user for : Principal(P) ,Rate(R), Time(T).Convert all to float and compute simple interest:  
# P = float(input("Enter Principal "))
# R = float(input("Enter Rate "))
# T = float(input("Enter Time "))

# SI = (P * R * T) / 100

# print("Simple Interest = " , SI)

# -------------------------------------------------------------------

#que 10 Take a decimal number as input (like 45.43)and output its       •integerpart-45
# •fractionalpart-.43

num = float(input("Enter a decimal value: 34.54"))

integer_part = int(num)
float_part = round(num - integer_part,2)  #2 means round off krkee bs . k bs 2 digits tak hi do

print("Integer part = ", integer_part )
print("Float part = ", float_part)



 