# Assignment 9
# Conversion Menu"

print("Conversion Menu:")

# Main Menu Function
def menu():
    print("1. Convert feet to inches")
    print("2. Convert yards to feet")
    print("3. Convert miles to yards")
    print("4. Convert miles to feet")
    print("5. Exit")
    print(" ")
    option = int(input("Please choose a menu option: "))

    # If Statements Used To Select Menu Options
    if option == 1:
        print(" ")
        inches_feet()
        print(" ")
        menu() # Calls Menu Back

    elif option == 2:
        print(" ")
        feet_yards()
        print(" ")
        menu()

    elif option == 3:
        print(" ")
        yards_miles()
        print(" ")
        menu()

    elif option == 4:
        print(" ")
        feet_miles()
        print(" ")
        menu()

    elif option == 5:
        print("Goodbye.")

# Conversion of feet to inches Function
def inches_feet():
    feet = int(input("Enter number of feet: "))
    inches = feet * 12
    conversion_one = print("There are", inches , "inches in", feet , "feet.")
    return conversion_one
    menu()


# Conversion of yards to feet Function
def feet_yards():
    yards = int(input("Enter number of yards: "))
    feet2 = yards * 3
    conversion_two = print("There are", feet2, "feet in", yards, "yards")
    return conversion_two
    menu()


# Conversion of Miles to Yards Function
def yards_miles():
    miles = int(input("Enter number of miles: "))
    yards1 = miles * 1760
    conversion_three = print("There are", yards1, " feet in", miles, "miles")
    return conversion_three
    menu()


# Conversion of Miles to Feet Function
def feet_miles():
    m = int(input("Enter number of miles: "))
    feet3 = m * 5280
    conversion_four = print("There are", feet3, "feet in", m, "miles")
    return conversion_four
    menu()


menu()