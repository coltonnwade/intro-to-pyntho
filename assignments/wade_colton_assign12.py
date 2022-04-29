# Colton Wade
# Assignment 12

# Enter File
filename = input("Enter the name of the file: ")

file = open(filename, "r")

# Display the lines of a file
line = file.readline().rstrip()

# Only display the first 6 lines of a file
for i in range(6):
    print(line)
    line = file.readline().rstrip()

# Close the file
file.close()




