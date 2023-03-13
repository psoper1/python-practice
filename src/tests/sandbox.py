# name = input("What is your name?")
# welcome_greeting = "Hello, Preston!"
# unwelcome_greeting = "You're not Preston!"

# def say_hello():
#     if name == "Preston":
#         print(welcome_greeting)
#         return welcome_greeting
#     else:
#         print(unwelcome_greeting)
#         return unwelcome_greeting
    
# say_hello()

# Do math

initial = input("Want to do some math? ('y' for Yes and 'n' for No) ")

if initial == "y":
    yes = input("What kind of math would you like to do? (A)ddition, (S)ubtraction, (M)ultiplication or (D)ivision? ")
    if yes == "A":
        first = input("First number: ")           
        second = input("Second number ")
        print(int(first) + int(second))
    elif yes == "S":
        first = input("First number: ")           
        second = input("Second number: ")
        print(int(first) - int(second))
    elif yes == "M":
        first = input("First number: ")           
        second = input("Second number: ")
        print(int(first) * int(second))
    elif yes == "D":
        first = input("First number: ")           
        second = input("Second number: ")
        print(int(first) / int(second))
            
elif initial == "n":
        print("Aww, no maths? :(")