def string_checker(question, valid_ans_list, num_letters):
    # checks the user enters the full word or the first letter of a word from a list of valid responses
    while True:
        response = input(question).lower()

        for i in valid_ans_list:
            if response == i:
                return i
            elif response == i[:num_letters]:
                return i
        print(f"\nplease choose an option from {valid_ans_list}\n")
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

like_coffee =string_checker("Do you like coffee? ", yes_no_list, 1)
print(f"\n{like_coffee} was chosen\n")
pay_method = string_checker("payment method: ", payment_list, 2)
print(f"\n{pay_method} was chosen")