# Description: This is the second script for Python programming.
age = 28  # integer variable
height = 6.0  # float variable (you can use decimal for a float)
name = "Ryan"  # string variable
is_programmer = True  # boolean variable

# Control Flow (if-Else statement)
if age < 18:  # Check if the person is a minor
    print("You're a minor.")  # Correct message
else:
    print("You're an adult.")  # Correct message

# Loops (For and While):
# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Functions
def greet(name):  # Correct indentation for function
    return f"Hello, {name}!"

print(greet("Ryan"))  # Call the greet function here

# Greet user function
def greet_user():
    name = input("What's your name? ")
    print(f"Hello, {name}! Welcome to Python.")

# Main block
if __name__ == "__main__":
    greet_user()  # Call greet_user only once
    print("This is the first script.")