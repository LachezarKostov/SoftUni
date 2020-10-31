film = input()
global_standard = 0
global_students = 0
global_kids = 0


while film != "Finish":
    free_space = int(input())
    filled_space = 0
    while filled_space < free_space:
        ticket = input()

        if ticket == "standard":
            filled_space += 1
            global_standard += 1
        elif ticket == "student":
            filled_space += 1
            global_students += 1
        elif ticket == "kid":
            filled_space += 1
            global_kids += 1
        elif ticket == "End":
            break
    precent_full = filled_space*100 / free_space
    print(f"{film} - {precent_full:.2f}% full.")
    film = input()

total_tickets = global_standard + global_kids + global_students
percent_standard = global_standard*100 / total_tickets
percent_students = global_students*100 / total_tickets
percent_kids = global_kids*100 / total_tickets


print(f"Total tickets: {total_tickets}")
print(f"""{percent_students:.2f}% student tickets.
{percent_standard:.2f}% standard tickets.
{percent_kids:.2f}% kids tickets.""")