def string_checker(question, valid_answer_list):
    #checks that users enter a full word or the first letter of a word from a list of valid responses

    while True:
        response = input(question).lower()

        for item in valid_answer_list:

            #checks if user enters a full word
            if response == item:
                return item

            # checks if user enters the first letter
            elif response == item[0]:
                return item
        print(f"Please enter a option from {valid_answer_list}.")

levels = ['easy', 'medium', 'hard']

like_coffee = string_checker("Do you like coffee? ", ['yes', 'no'])
print(f"you chose {like_coffee}")
choose_level = string_checker("choose a level ", levels)
print(f"you chose {choose_level}")
