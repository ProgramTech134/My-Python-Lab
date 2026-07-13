# Challenge 1: E-commerce Discount Alert
# Statement:
# You have a list of products in an online store:
# products = ["Tote Bag", "Clay Pot", "Canvas", "Yarn", "Paint Brush"]

# Write a for loop that prints each product one by one.

# Condition:

# If the product name is "Canvas", print the name along with the text " - 20% OFF!".

# For all other products, just print their normal name.

#_____________________________________________________________________________________________________
#_________________________________SOLUTION____________________________________________________________
#_____________________________________________________________________________________________________


products = ["tote bags" , "clay pot" , "canvas" , "yarn" , "paint brush"] 
for i in products :
    print(i)
    if(i == "canvas") :
       print("- 20% OFF!")
