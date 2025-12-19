color = input("Enter Banana Color: ").lower()

if color == "green":
    print("Not ripe.")
elif color == "yellow":
    print("Perfectly ripe!")
elif color in ["brown", "black"]: # Checks if color is either brown OR black
    print("Overripe.")
else:
    print("That is an unusual color for a banana!")
