#EVENT ADMISSION

guest = ["chinaza", "precious", "Amara", "ozy"]

event_Quest_1 = input("please input your name: \n")
if event_Quest_1 not in guest:
    print(f"You are not invited {event_Quest_1},please leave the venue.")
if event_Quest_1 in guest:
    event_Quest_2 = input(f"welcome {event_Quest_1}, Please are you married: \n")
    if event_Quest_2 == "yes":
            print("Welcome, Access granted!!")
    else:
        print(f"please hold on {event_Quest_1}")