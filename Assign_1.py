Gayatri Khatekar

Assignment No.- 01
-----------------------------------------------
Q.1 print helloworld

print("Hello World")


O/P: Hello World

--------------------------------------------------------------------------------------------------------------------

Q.2 Write a code that describe Indentation error

def greet(name):
print(f"Hello, {name}!")  

O/P: Cell In[2], line 4
    print(f"Hello, {name}!")
    ^
IndentationError: expected an indented block after function definition on line 3

--------------------------------------------------------------------------------------------------------------------

Q.4 write a code that describe local and global variable with same name

x = 10

def my_function():
    x = 5
    print("Value of x inside the function (local variable):", x)

my_function()
print("Value of x outside the function (global variable):", x)


O/P Value of x inside the function (local variable): 5
Value of x outside the function (global variable): 10

--------------------------------------------------------------------------------------------------------------------


Q.5 Write a code for string, int and float input.

# Taking a string input
name = input("Enter your name: ")

# Taking an integer input
age = int(input("Enter your age: "))

# Taking a float input
height = float(input("Enter your height in meters: "))

# Displaying the inputs
print("\n--- User Details ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height:.2f} meters")

O/P: 
Enter your name:  Gayatri
Enter your age:  22
Enter your height in meters:  160

--- User Details ---
Name: Gayatri
Age: 22
Height: 160.00 meters

