# Colton Wade
# Lab 11
# Lists

# 1. Creating a List
my_list = ["Blue", "Green", "Red", "Purple", "Orange"]

# 2. Iterate over the list, printing each item in the list

# getting the length of the list
length = len(my_list)

# Iterating the list
for i in range(length):
    print(my_list[i])
print(len(my_list))
print(" ")


# 3. Add an item to the list
my_list.append("Yellow")

# 4. Print the length of the list

# getting the new length of the list
length = len(my_list)

# Iterating the new list
for a in range(length):
    print(my_list[a])
print(len(my_list))
print(" ")

# 4. Delete an item from the list.
my_list.remove("Green")

# 5. Print the length of the list
length = len(my_list)

for r in range(length):
    print(my_list[r])
print(len(my_list))
print(" ")
