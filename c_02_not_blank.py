def not_blank(question):
    #checks that a users response is not blank

    while True:
        response = input(question)
        if response != '':
            return response
        print("Sorry, this Can't be blank. Please try again.")


who = not_blank("please enter your name")
print(f"hello {who}.")