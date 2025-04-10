import random

char = "abcdefghijklmnopqrstuvwxyz"
upperchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
specialchar = "!@#$%^&*()_+[]{}|;:,.<>?"

# Get input from the user
numberofchar = int(input("Enter the length of the password: "))
numberofupperchar = int(input("Enter the number of uppercase letters: "))
numberofdigits = int(input("Enter the number of digits: "))
numberofspecialchar = int(input("Enter the number of special characters: "))

# Check if the sum of the character types is greater than or equal to the specified password length
if numberofupperchar + numberofdigits + numberofspecialchar > numberofchar:
    print("The sum of uppercase letters, digits, and special characters exceeds the total password length.")
    exit(1)

# Initialize the password list
password = []

# add the required number of each character type to the password list
password += random.sample(char, numberofchar - numberofupperchar - numberofdigits - numberofspecialchar)
password += random.sample(upperchar, numberofupperchar)
password += random.sample(digits, numberofdigits)
password += random.sample(specialchar, numberofspecialchar)

# Shuffle the password to make it more random
random.shuffle(password)

# Convert the list into a string and display the password
password = ''.join(password)
print("Your password is: " + password)
