#Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name: ")

    #if name is exit code, break the loop
    if name == "exit code":
        break
    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"The maximum amount of tickets has been sold ({MAX_TICKETS} tickets)")
else:
    print(f"The total number of tickets is {tickets_sold}/{MAX_TICKETS}")