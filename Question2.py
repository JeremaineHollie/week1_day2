# Task 1 & 2

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 elif "conference room"
# print(venue)

attendees = int(input("Enter number of attendees: "))
venue = "large hall" 
if attendees > 100: 
    print(venue)
else:
    print("conference room")
food = input("Do you want vegetarian food? ")
if food == "yes":
    print("Great! I know a great caterer by the name of Veggie Delight Caterers!")
else:
    print("Oh okay! I highly recommend 'Gourmet Meals Caterers if you would like a normal option!")
