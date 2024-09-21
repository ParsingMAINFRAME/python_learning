#Basic variables example
age = 28 #integer variable
height = 6 #float variable
name = "Ryan" #string variable
is_Programmer = True #boolean variable

#Control Flow (if-Else  statement)
age = 28

if age < 18:
    print("you're an adult.")   
else:
    print("you're a minor.")
#Loops (For and While):
#For loop
for i in range(5):
    print(i)

#While loop
count = 0 
while count < 5:
    print(count)
    count += 1
#Functions
def greet(name):
    return f"Hello, {name}!"
    
print(greet("Ryan"))
if __name__ == "__main__":
    print("This is the first script.")
#greet user function
def greet_user():
    name = input("What's your name? ")
    print(f"Hello, {name}! Welcome to Python.")

    #use __name__ == :__main__" to run only if script is executed directly
    #main block
if __name__== "__main__":
        greet_user()    #call the function
        print("This is the first script.")