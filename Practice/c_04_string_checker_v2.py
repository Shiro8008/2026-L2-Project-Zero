def string_checker(question, valid_answer_list, num_letters):
    #checks that users enter a full word or the 'n' letter of a word from a list of valid responses

    while True:
        response = input(question).lower()

        for item in valid_answer_list:

            #checks if user enters a full word
            if response == item:
                return item

            # checks if user enters the first letter
            elif response == item[:num_letters]:
                return item
        print(f"Please enter a option from {valid_answer_list}.")

yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

like_coffee = string_checker("Do you like coffee? ", yes_no_list, num_letters = 1)
print(f"you chose {like_coffee}")
payment_method = string_checker("payment method: ", payment_list, num_letters = 2)
print(f"you {payment_method}")