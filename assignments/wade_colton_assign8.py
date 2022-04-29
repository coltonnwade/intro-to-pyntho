#Assignment 8
#Sum Vowels

#Defining the Function
def vowels():

    #Defining the Variable
    counta = 0
    counte = 0
    counti = 0
    counto = 0
    countu = 0

#Input
    string = input(" ")

    #For Loop
    for ch in string:

        #If Statement's for the letters
        if ch == "A" or ch == "a":
            counta += 1

        if ch == "E" or ch == "e":
            counte += 1

        if ch == "I" or ch == "i":
            counti += 1

        if ch == "O" or ch == "o":
            counto += 1

        if ch == "U" or ch == "u":
            countu += 1

    #Print's the Number of Vowels
    print("A:", counta)
    print("E:", counte)
    print("I:", counti)
    print("O:", counto)
    print("U:", countu)

#Calls the function
vowels()