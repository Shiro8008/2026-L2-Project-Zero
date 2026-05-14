def string_checker(question, valid_ans_list):
    # checks the user enters the full word or the first letter of a word from a list of valid responses
    while True:
        response = input(question).lower()

        for i in valid_ans_list:
            if response == i:
                return i
            elif response == i[0]:
                return i
        print(f"\nplease choose an option from {valid_ans_list}\n")
levels = ['easy', 'medium', 'hard']
like_coffee =string_checker("Do you like coffee? ",['yes', 'no'])
print(f"\n{like_coffee} was chosen\n")
chose_level = string_checker("choose a level... ", levels)
print(f"\n{chose_level} was chosen")