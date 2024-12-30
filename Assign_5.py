Gayatri Khatekar

Assignment-05(Function)
--------------------------------------------------------------------------------
Q. 1.Declare a div() function with two parameters. Then call the function and pass two numbers and display their division. 

def div(num1, num2):

    if num2 != 0:
        result = num1 / num2
        print(f"The division result of {num1} by {num2} is: {result}")
    else:
        print("Error! Division by zero is not allowed.")

# Call the div() function and pass two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

div(num1, num2)

O/P:
Enter the first number:  67
Enter the second number:  45
The division result of 67.0 by 45.0 is: 1.488888888888889
----------------------------------------------------------------------------------------------------------------------------------------

Q.2 Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number . 

def square(num):
    result = num ** 2
    print(f"The square of {num} is: {result}")

# Call the square() function and pass one number
num = float(input("Enter a number: "))
square(num)

O/P:
Enter a number:  25
The square of 25.0 is: 625.0
--------------------------------------------------------------------------------------------------------------

Q. 3.Using max() and min() functions display the maximum and minimum of 5 random numbers.

import random
random_numbers = [random.randint(1, 100) for _ in range(5)]

# Display the random numbers
print(f"Random numbers: {random_numbers}")

# Find and display the maximum and minimum numbers
max_num = max(random_numbers)
min_num = min(random_numbers)

print(f"The maximum number is: {max_num}")
print(f"The minimum number is: {min_num}")

O/P:
Random numbers: [27, 44, 95, 22, 83]
The maximum number is: 95
The minimum number is: 22
-------------------------------------------------------------------------------------------------------------------

Q.4.Accept a name from the user and display that in lower case using lower() function

name = input("Enter your name: ")

# Converting the name to lowercase
lowercase_name = name.lower()
print(f"Your name in lowercase is: {lowercase_name}")

O/P:
Enter your name:  Gayatri
Your name in lowercase is: gayatri