def yes_no(question):
    #checks if user enters yes, y, no, n to a question

    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes (y) or no (n)")\



while True:
    want_instructions = yes_no("do you want to read the instructions?")
    print(f"you chose {want_instructions}")