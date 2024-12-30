Gayatri Khatekar
Assignment-04(Control Statements)
--------------------------------------------------------------------------------------------------------------------------------
Q.1. Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

O/P:
Enter a number:  16
Even
-------------------------------------------------------------------------------------------------------------------------------

Q.2. Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

O/P:
Enter your age:  22
You are eligible to vote.
---------------------------------------------------------------------------------------------------------------------------------


Q.3. Write a Python program that determines if a given year is a leap year or not.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

O/P:
Enter a year:  2017
2017 is not a leap year.
--------------------------------------------------------------------------------------------------------------------------------------

Q.4. Create a Python program that checks if a user-given number is positive, negative, or zero.

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

O/P:
Enter a number:  22
The number is positive.
----------------------------------------------------------------------------------------------------------------------------------------

Q.5 Write a Python program that determines the largest of three numbers entered by the user.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}.")

O/P:
Enter the first number:  16
Enter the second number:  37
Enter the third number:  27
The largest number is 37.0.
