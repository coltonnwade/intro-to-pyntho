# Lab 14
# Colton Wade


# Function that checks if email is valid
def is_valid_email(email_address):

    # Sets variables to false
    valid_email = False
    has_at = False
    has_end = False

    # It checks the email address for the @ sign
    # If @ is in the email address it will set the variable has_at to True
    if "@" in email_address:
        has_at = True

    # It checks and sees if the email ends with .edu
    # If the email ends with .edu it will set the variable has_end to True
    if email_address.endswith(".edu"):
        has_end = True


    # It goes through and checks if has_at and has_end is true
    # If the email has both the @ sign and ends with .edu it is a valid email and will set valid_email to True
    if has_at and has_end:
        valid_email = True



    # Returns the value valid_email
    return valid_email

# Main Function tht goes through the valid email function and checks if email is valid
# Prints the result True or False
def main():
    email = "coltonwade@volstate.edu"
    valid_email = is_valid_email(email)
    print(valid_email)

main()
