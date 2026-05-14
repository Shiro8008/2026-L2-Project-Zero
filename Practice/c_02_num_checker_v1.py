def num_check(question,num_type, exit_code=None):
    if num_type == "integer":
        error = "Oops - Please enter a integer higher than zero"
        change_to = int
    else:
        error = "Oops - Please enter a number higher than zero"
        change_to = float

    while True:
        response = input(question).lower()


        if response == exit_code:
            return response
        try:
            response = change_to(response)
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)
while True:
    print()

    my_float = num_check("Please enter a number higher than zero: ", "float")
    print(f"thanks you chose {my_float}")
    print()
    my_int = num_check("Please enter a number higher than zero: ", "integer", "")

    if my_int == "":
        print("you have chosen infinite mode.")
    else:
        print(f"Thanks. you chose {my_int}")