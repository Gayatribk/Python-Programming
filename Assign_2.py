Gayatri Khatekar

Assignment -02 (Operator)
---------------------------------------------------------
Q.1 Write a program for arithmatic operators

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2  # Addition
subtraction = num1 - num2  # Subtraction
multiplication = num1 * num2  # Multiplication
division = num1 / num2  # Division
modulus = num1 % num2  # Modulus
exponent = num1 ** num2  # Exponentiation
floor_division = num1 // num2  # Floor Division

print("\n--- Arithmetic Operations ---")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Modulus: {num1} % {num2} = {modulus}")
print(f"Exponentiation: {num1} ** {num2} = {exponent}")
print(f"Floor Division: {num1} // {num2} = {floor_division}")

O/P: 
Enter the first number:  12
Enter the second number:  2

--- Arithmetic Operations ---
Addition: 12.0 + 2.0 = 14.0
Subtraction: 12.0 - 2.0 = 10.0
Multiplication: 12.0 * 2.0 = 24.0
Division: 12.0 / 2.0 = 6.0
Modulus: 12.0 % 2.0 = 0.0
Exponentiation: 12.0 ** 2.0 = 144.0
Floor Division: 12.0 // 2.0 = 6.0

-----------------------------------------------------------------------------

Q.2 Write a program for assignment operators

x = int(input("Enter an initial value for x: "))

print("\n--- Assignment Operations ---")
x += 5  # Add and assign
print(f"x += 5: {x}")

x -= 3  # Subtract and assign
print(f"x -= 3: {x}")

x *= 2  # Multiply and assign
print(f"x *= 2: {x}")

x /= 4  # Divide and assign
print(f"x /= 4: {x}")

x %= 3  # Modulus and assign
print(f"x %= 3: {x}")

x **= 2  # Exponentiation and assign
print(f"x **= 2: {x}")

x //= 2  # Floor division and assign
print(f"x //= 2: {x}")

O/P:
Enter an initial value for x:  16

--- Assignment Operations ---
x += 5: 21
x -= 3: 18
x *= 2: 36
x /= 4: 9.0
x %= 3: 0.0
x **= 2: 0.0
x //= 2: 0.0

---------------------------------------------------------------------

Q.3 Write a program for Bitwise operators 

# Taking two integers as input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Demonstrating bitwise operators
print("\n--- Bitwise Operations ---")
print(f"num1: {num1}, num2: {num2}")

# AND
result = num1 & num2
print(f"Bitwise AND (num1 & num2): {result}")

# OR
result = num1 | num2
print(f"Bitwise OR (num1 | num2): {result}")

# XOR
result = num1 ^ num2
print(f"Bitwise XOR (num1 ^ num2): {result}")

# NOT
result = ~num1
print(f"Bitwise NOT (~num1): {result}")

O/P:
Enter the first number:  25
Enter the second number:  16

--- Bitwise Operations ---
num1: 25, num2: 16
Bitwise AND (num1 & num2): 16
Bitwise OR (num1 | num2): 25
Bitwise XOR (num1 ^ num2): 9
Bitwise NOT (~num1): -26

-------------------------------------------------------------------------

Q.4 Write a program to calculate greatest of three numbers.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

print(f"\nThe greatest number is: {greatest}")

O/P:
Enter the first number:  16
Enter the second number:  2
Enter the third number:  5

The greatest number is: 16.0

--------------------------------------------------------------------------------------

Q.6  Calculate the area of a circle.

import math
radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2

print(f"The area of the circle with radius {radius} is: {area:.2f}")

O/P: 
Enter the radius of the circle:  16
The area of the circle with radius 16.0 is: 804.25
----------------------------------------------------------------------------------------

Q.7 Calculate the area of a triangle.

def main():
    print("Calculate the area of a triangle using the base and height.")
    
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    
    area = area_base_height(base, height)
    print(f"The area of the triangle is: {area}")

if __name__ == "__main__":
    main()

O/P:

Calculate the area of a triangle using the base and height.
Enter the base of the triangle:  19
Enter the height of the triangle:  13
The area of the triangle is: 123.5
-----------------------------------------------------------------------------------------

