Gayatri Khatekar
Assignment-06(While Loop)
---------------------------------------------------------------------------------------------
Q.1 Print the table of 5 using for loop

for i in range(1, 11):  # Loop from 1 to 10
    print(f"5 x {i} = {5 * i}")

o/p:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
------------------------------------------------------------------------------------------------------------
Q.2 Print even number series by taking input from the user:

limit = int(input("Enter the range limit: "))

print("Even number series:")
for i in range(2, limit + 1, 2):  # Start from 2, go up to the limit, step by 2
    print(i)

o/p:
Enter the range limit:  10
Even number series:
2
4
6
8
10
----------------------------------------------------------------------------------------------------------------------------

 Q.3 Create a list and iterate through its items using a for loop:

fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

print("List of fruits:")
for fruit in fruits:
    print(fruit)

O/P:
List of fruits:
Apple
Banana
Cherry
Date
Elderberry
---------------------------------------------------------------------------------------------------------------------------------
Q.4 Calculate the sum of numbers from 1 to 10 

total_sum = 0

for i in range(1, 11):
    total_sum += i

print(f"The sum of numbers from 1 to 10 is: {total_sum}")

O/P:
The sum of numbers from 1 to 10 is: 55
------------------------------------------------------------------------------------------------------------------

Q. 5. print the pattern   

          *

         ***

       *****

      *******

     *********

rows = 5

for i in range(1, rows + 1):
    
    print(" " * (rows - i), end="") # Print spaces
    
    print("*" * (2 * i - 1)) # Print stars

O/P:
    *
   ***
  *****
 *******
*********
--------------------------------------------------------------------------------------------------------------------------------------------

Q.6  Print the first 10 natural numbers using for loop 

print("The first 10 natural numbers are:")
for i in range(1, 11):  # Loop from 1 to 10
    print(i)

O/P:
The first 10 natural numbers are:
1
2
3
4
5
6
7
8
9
10
------------------------------------------------------------------------------------------------------------------------------------------------------

Q.7 Python program to check if the given string is a palindrome

def is_palindrome(s):
    
    s = s.replace(" ", "").lower()
    # Check if the string is the same as its reverse
    return s == s[::-1]

user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")

O/P:
Enter a string:  madam
'madam' is a palindrome.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Q.8 Python program to check if a given number is an Armstrong number

def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    return sum_of_powers == num

user_input = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong_number(user_input):
    print(f"{user_input} is an Armstrong number.")
else:
    print(f"{user_input} is not an Armstrong number.")

O/P:
Enter a number:  153
153 is an Armstrong number.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Q.9 Python program to get the Fibonacci series between 0 to 50 

def fibonacci_series(limit):
    a, b = 0, 1

    while a <= limit:
        print(a, end=" ")
        a, b = b, a + b  # Update the values of a and b

# Call the function with the limit of 50
fibonacci_series(50)

O/P:
0 1 1 2 3 5 8 13 21 34 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Q.10 Python program to check the validity of password input by users

import re

def is_valid_password(password):
    # Check password length
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    
    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."
    
    # Check for at least one digit
    if not re.search(r"\d", password):
        return "Password must contain at least one digit."
    
    # Check for at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>)."
    
    # If all conditions are met
    return "Password is valid."

# Take input from the user
user_password = input("Enter your password: ")

# Check the validity of the password
result = is_valid_password(user_password)
print(result)

O/P:
Enter your password:  Gayatribk@22
Password is valid.
