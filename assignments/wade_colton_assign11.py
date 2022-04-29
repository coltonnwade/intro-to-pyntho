# Colton Wade
# Assignment 11
# Lists

# Starting List called Numbers
numbers = [74, 95, -20, 250, 126, 50, -5, 30, 87, 67]

# Loop to build another list called Valid_Numbers
# Adds any numbers in list "numbers" 1-100 to new valid_numbers list
valid_numbers = []
if numbers[0]  > 0 and numbers[0] < 100:
    valid_numbers.append(numbers[0])

if numbers[1] > 0 and numbers[1] < 100:
    valid_numbers.append(numbers[1])

if numbers[2] > 0 and numbers[2] < 100:
    valid_numbers.append(numbers[2])

if numbers[3] > 0 and numbers[3] < 100:
    valid_numbers.append(numbers[3])

if numbers[4] > 0 and numbers[4] < 100:
    valid_numbers.append(numbers[4])

if numbers[5] > 0 and numbers[5] < 100:
    valid_numbers.append(numbers[5])

if numbers[6] > 0 and numbers[6] < 100:
    valid_numbers.append(numbers[6])

if numbers[7] > 0 and numbers[7] < 100:
    valid_numbers.append(numbers[7])

if numbers[8] > 0 and numbers[8] < 100:
    valid_numbers.append(numbers[8])

if numbers[9] > 0 and numbers[9] < 100:
    valid_numbers.append(numbers[9])

# prints valid_numbers list
print(valid_numbers)

# Adds total and Average of valid_numbers list and prints them
total = 0

for number in valid_numbers:
    total = total + number

print("Total: ", total)
print("Average: ", total / len(valid_numbers))