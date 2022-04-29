# Assignment 6
# With this assignment i had to rely on youtube tutorials more than the book
# I couldn't find good examples in the book. Lines 7 and 8 took me forever to figure out
total = 0
d = int(input("How many days did you collect gems?"))
for g in range (1, d +1):
    print("How many gems did you collect on day",  g , end = ' ')
    gems_collected = float(input(': '))
    total += gems_collected
print("Total Gems Collected: ", total)

avg = total / d
print("Average Gems Collected: ", avg)



