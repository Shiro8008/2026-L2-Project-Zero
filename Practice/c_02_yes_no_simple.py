def yes_no(question):
    # checked if the user entered yes / y or no / n

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please respond with 'yes' or 'no'\n")


while True:
    want_instructions = yes_no("Do you want to read the instructions?")
    print(f"you chose {want_instructions}\n")