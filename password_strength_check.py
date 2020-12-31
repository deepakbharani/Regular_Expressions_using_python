# Author:   Bharani Deepak
# Date:     30.12.2020
# Title:    Passwort strength check

# HOW TO USE:
# Enter the password to be checked in variable "password" -> Run the code

import re

def password_check(pw,char_class):
    # This function creates regex object and match the character class with the password
    try:
        capexp = re.compile(char_class)
        MOcapexp = capexp.search(pw).group()
        return 1

    except AttributeError:
        if char_class == '\d':
            print("Password must have atleast one digit")
        else:
            print("Password must have atleast one",char_class)

def strength_check(checklist):
    # This function checks the strength of the password
    if len(checklist) == 3:
        print("Password is very strong")
    elif len(checklist) == 2:
        print("Password is medium strong")
    else:
        print("Password is weak")

def main():
    password = 'pass_Word123'                                   # Enter your password here
    char_class = ['[A-Z]','\d','[$&+,:;=?@#\-|\'<>.^*()%!_]']   # [A-Z] -> Checks for Capital letters in password
                                                                # \d    -> Checks for digits in password
                                                                # [$&+,:;=?@#|\'<>.-^*()%!_] -> Checks for special char

    if ((len(password) >= 8) and (len(password) <= 12)):        # Checks for valid password length (8-12)
        checklist = []                                          # list to store satisfied char_classes
        for i in range(len(char_class)):                        # run a loop through the test cases (char_class)
            check = password_check(password,char_class[i])
            if check == 1:
                checklist.append(check)
        strength_check(checklist)

    elif (len(password) >= 12):
        print("Password must not be more than 12 digits long")
    else:
        print("Password must be atleast 8 digits long")

if __name__ == "__main__":
    main()

