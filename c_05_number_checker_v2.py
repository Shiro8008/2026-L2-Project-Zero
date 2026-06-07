def int_checker(question):
    #checks if users entered an integer between two values

    while True:
        error = "Please enter a integer"
        #checks for exit code

        try:
            #change the response to an integer
            response = int(input(question))
            return response

        except ValueError:
            print(error)

while True:
    print()

    #asks user for their name
    name = input("Please enter your name: ") #replace with call  to 'not blank' function

    # asks for their age and checks if it's between 12 and 120
    age = int_checker("please enter your age: ")
    #output error message / success message
    if age < 12:
        print("Your too young")
        continue
    elif age > 120:
        print("Your too old")
        continue
    else:
        print(f'{name} has successfully bought a ticket')