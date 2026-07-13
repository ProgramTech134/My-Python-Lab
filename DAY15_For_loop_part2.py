# _______________Challenge 2: Website Username Validator____________________
# Statement:
# When a user creates an account on a website, we need to check
# if their username contains any invalid characters.
# Take a string variable: username = "user_@123"

# Write a for loop to check each character of the string one by one.

# Condition:

# If the loop finds the character "@" anywhere in the string,
# print the error message: "Error: Special characters not allowed!"

#______________________SOLUTION____________________________________

username = "user_@123"
for i in username :
    if(i == "@") :
        print("Error: Special characters not allowed!")
        
    else :
        print(i)