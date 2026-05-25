def num_checker(question, num_type, exit_code=None):
    #checks if users entered an integer / float that is more than zero (or the optional exit code)
    error = "Please enter a integer more than zero"
    if num_type == 'integer':
        print(error)
        change_to = int
    else:
        print(error)
        change_to = float

    while True:
        response = input(question).lower()

        #checks for exit code
        if response == exit_code:
            return response

        try:
            #change the response to an integer and check that it's more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


while True:
    my_float = num_checker("Enter a number more than 0: ", "float")
    print(f"Thanks, you chose {my_float}.")
    my_int = num_checker("Enter a integer more than 0: ", "integer" ,"")

    if my_int == "":
        print("infinite mood chosen.")
    else:
        print(f"Thanks, You chose {my_int}.")