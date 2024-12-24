Gayatri Khatekar

Assignment- 03 (Programming Statements)
----------------------------------------------------------------------------------------------------------------------------------

Q.1 . Using input() function take one number from the user and using ternary operators check whether the number is even or odd 

num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(f"The number is {result}.")

O/P: Enter a number:  17
The number is Odd.
-----------------------------------------------------------------------------

Q.2. Using input function take two number and then swap the number 

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

num1, num2 = num2, num1

print(f"After swapping: First number = {num1}, Second number = {num2}")

O/P:
Enter the first number:  16
Enter the second number:  17
After swapping: First number = 17, Second number = 16
------------------------------------------------------------------------------------

Q.3 Write a Program to Convert Kilometers to Miles 

kilometers = float(input("Enter distance in kilometers: "))

# Conversion factor from kilometers to miles
miles = kilometers * 0.621371

print(f"{kilometers} kilometers is equal to {miles} miles.")

O/P: 
Enter distance in kilometers:  34
34.0 kilometers is equal to 21.126614 miles.
---------------------------------------------------------------------------------

 Q. 4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.

P = 200  # Principal amount
R = 5    # Rate of interest per year
T = 5    # Time in years

SI = (P * R * T) / 100

print(f"The Simple Interest is Rs. {SI}.")

O/P:
The Simple Interest is Rs. 50.0.