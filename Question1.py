# Task 1, 2, & 3

# place = input("Choose a place: forest or cave? ")

# if place = "forest":
#    action = input("climb a tree or cross a river?")
#    if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river":
#         print("You found a boat!")
# elif place = "cave":
#     print("You find a hidden treasure!")

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("Would you like to light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You've found a hidden treasure!")
    elif action == "proceed in the dark":
        action = input("You've bumped into something really hard! Please light a torch to find out what it is! Please enter 'torch' to light it! ")
        if action == "torch":
            print("You've found a hidden treasure!")
        else:
            pass
else:
    pass