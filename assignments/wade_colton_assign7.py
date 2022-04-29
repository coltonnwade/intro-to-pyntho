#ASSIGNMENT 7
maxnumber = int(input("Enter the value for the maximum number:"))                   #Where you enter the Maximum Number
#
total = 0
totalnum = 0

while maxnumber >= 0: #While Loop
    print("Enter a number between 1 and", maxnumber, end='')                        #ask to enter more numbers
    total = float(input(": "))
    if total >= 0 and total <= maxnumber:                                           #If the number is above the Maxnumber or Negative it will not count into the sum
        totalnum += total
    if total <= 0:                                                                  #If number entered is negative it will end the loop and calculate the Sum
        print("Sum of all valid numbers you entered:", totalnum)
        break                                                                       #Ends the loop
    if total > maxnumber:                                                           #If the Number entered is above the Maxnumber it will print Invalid Number
        print("Invalid Number")
