#NestedbLoop Lab 7
#
num = int(input("Enter the maximum number for the multiplication table:"))
for m in range (1, num + 1): #outer loop
    for i in range(1, num + 1): #inner loop
        print("{0} * {1} = {2}". format(m, i, (m * i)))

