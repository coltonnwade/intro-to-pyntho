# Lab 9
# Is Equal Function
def is_equal(firstnum, secondnum):
    # If Statement

    # If The Numbers are Equal It is True, If Not It is False
    if firstnum == secondnum:
        status = True
    else:
        status = False

    # Returns Boolean Values
    return status


# Calls Back Function
equal = is_equal(2, 3)  # Input Integers

#Changes True/False to Equal/Not Equal
if equal == True:
    print("Equal")
else:
    print("Not Equal")