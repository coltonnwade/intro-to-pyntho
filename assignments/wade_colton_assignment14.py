# Assignment 14
# Colton Wade

# Silly Encryption Code

# Defines Silly Encryption Function

def silly_encrypter(input):
    # If statement that requires all input to be uppercase
    if english_input.isupper():

        # Splits the sentence up into a list
        string = input.split(" ")
        sentence = ""

        # Encrypts each word in the list
        # Replacing the first letter and the rest of the letters in the word
        # Also adding IE at the end of every word
        for word in string:
            first_letter = word[0]
            rest_of_letters = word[1:]
            encryption = rest_of_letters + first_letter + "IE"
            sentence = sentence + encryption + " "

        # Returns the value of sentence
        return sentence

    # If input is not uppercase it will print message
    else:
        print("Invalid Input")
        print("Must be uppercase!")


# Takes in English Input
english_input = input("English Input: ")

# Defines encrypted
encrypted_output = silly_encrypter(english_input)

# Prints encrypted output
print("Silly Encryption Output:", encrypted_output)