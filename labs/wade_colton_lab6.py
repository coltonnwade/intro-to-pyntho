#Lab 6 Loop 1
for num in [1, 2, 3, 4, 5, 6, 7,8, 9, 10]: #could also do "for num in range (1, 11):" but i found the one i used in the book
    print(num)

#Lab 6 Loop 2
status = True
while status==True:
    print("Energizer Bunny keeps on going and going... ")
    a = input("Would you like to print this again?")
    if a != "y": #

        status = False
