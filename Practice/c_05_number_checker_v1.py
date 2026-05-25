def int_checker(question):
    #checks if users entered an integer that is more than zero (or the 'XXX' exit code)
    error = "Please enter a integer more than zero"

    while True:
        response = input(question).lower()

        #checks for exit code
        if response == "XXX":
            return response

        try:
            #change the response to an integer and check that it's more than zero
            response = int(input(response))

            return response
        except ValueError:
            print(error)