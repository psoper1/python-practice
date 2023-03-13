name = input("What is your name?")
welcome_greeting = "Hello, Preston!"
unwelcome_greeting = "You're not Preston!"

def say_hello():
    if name == "Preston":
        print(welcome_greeting)
        return welcome_greeting
    else:
        print(unwelcome_greeting)
        return unwelcome_greeting
    
say_hello()