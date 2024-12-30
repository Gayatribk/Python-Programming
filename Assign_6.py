Gayatri Khatekar
Assignment-06(For Loop)
---------------------------------------------------------------------------------------------------------------------------------------------

1.Write a python program to reverse a number using a while loop. 

num = int(input("Enter a number: "))

# Initializing the reverse number to 0
reverse = 0

# Using a while loop to reverse the number
while num > 0:
    digit = num % 10  # Extract the last digit
    reverse = reverse * 10 + digit  # Add the digit to the reverse number
    num = num // 10  # Remove the last digit from the original number

print(f"The reversed number is: {reverse}")

O/P:
Enter a number:  45
The reversed number is: 54
-------------------------------------------------------------------------------------------------------------------------------------------------------

Q.2 2.Write a python program to check whether a number is palindrome or not?

num = int(input("Enter a number: "))

original_num = num

# Reversing the number using a while loop
reverse = 0
while num > 0:
    digit = num % 10  # Extract the last digit
    reverse = reverse * 10 + digit  # Add the digit to the reverse number
    num = num // 10  # Remove the last digit from the original number

# Checking if the original number is equal to the reversed number
if original_num == reverse:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")

O/P:
Enter a number:  455454
455454 is not a palindrome.
---------------------------------------------------------------------------------------------------------------------------------------------------------

Q.3.Write a python program finding the factorial of a given number using a while loop

num = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i  # Multiply factorial by i
    i += 1  # Increment i
print(f"The factorial of {num} is: {factorial}")

O/P:
Enter a number:  21
The factorial of 21 is: 51090942171709440000
-------------------------------------------------------------------------------------------------------------------------------------------------------

Q.4 Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers

total_sum = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    
    # If the user enters 0, break the loop
    if num == 0:
        break
    
    total_sum += num
    
print(f"The sum of all the numbers is: {total_sum}")

O/P:
Enter a number (0 to stop):  23
Enter a number (0 to stop):  34
Enter a number (0 to stop):  56
Enter a number (0 to stop):  12
Enter a number (0 to stop):  0
The sum of all the numbers is: 125
----------------------------------------------------------------------------------------------------------------------------------------------------------

Q.5  Program to check whether the given number is Armstrong or not.

num = int(input("Enter a number: "))

num_digits = len(str(num))

original_num = num

# Initializing a variable to store the sum of the digits raised to the power of num_digits
sum_of_powers = 0

while num > 0:
    digit = num % 10  # Extract the last digit
    sum_of_powers += digit ** num_digits  # Add the digit raised to the power of num_digits
    num = num // 10  # Remove the last digit from the number

if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")

O/P:
Enter a number:  23
23 is not an Armstrong number.
-------------------------------------------------------------------------------------------------------------------------------------------------
Q. 6.Program to find the factorial of a number.

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i  # Multiply factorial by i

print(f"The factorial of {num} is: {factorial}")

O/P:
Enter a number:  24
The factorial of 24 is: 620448401733239439360000