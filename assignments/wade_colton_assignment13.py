# Colton Wade
# Assignment 13


try:

    # Display the highest score

    # Opens grades file
    grades = open("grades.txt", "r")

    # Defines Variables
    high_score = 0
    high_name = ""

    # Finds the Highest Score
    for line in grades:
        # Splits the line up into name and score
        name,score = line.rstrip().split(";")

        # Finds the Person with the Highest Score
        if int(score) > high_score:
            high_score = int(score)
            high_name = name

    grades.close()

    print("Highest Score:", high_name, high_score)


    # Display the amount of records

    # Opens grades.txt file
    records = open("grades.txt", "r")

    # Defines Variable
    line_count = 0

    # Counts lines(records)
    for line in records:
        if line != "\n":
            line_count += 1
    records.close()

    print("Number of records:", line_count)

# # If the file doesnt exist it will display this error message
except IOError:
    print("An error occurred trying to read the filename")

# If there is a value other than a number it will display this error message
except ValueError:
    print("Non-Numeric data found in the file")