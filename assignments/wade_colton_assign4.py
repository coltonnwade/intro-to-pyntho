#Monster Game
monster = int(input("Enter the monster number:"))
if monster < 0 or  36 < monster:
    color = "error"
elif monster == 0:
    color = "purple"
elif monster <= 10 or 19 <= monster and monster <= 28:
    if monster % 2 == 0:
        color = "black"
    else:
        color = "blue"
else:
    if monster % 2 == 0:
        color ="blue"
    else:
        color = "black"
if color == "error":
    print("Error not a valid monster")
else:
    print("The monster color is:", color)