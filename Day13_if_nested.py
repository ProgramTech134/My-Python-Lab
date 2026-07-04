# The Problem: Online Delivery Fee Calculator
# Write a program that decides the shipping/delivery fee for a shopping app based on two things: the Total Order Amount and whether the user has a Premium Membership.
# Here are the rules:
# If the order amount is £50 or more:
# If the user has a Premium Membership, the delivery is Free (£0).
# If the user does NOT have a Premium Membership, the delivery fee is £2.
# If the order amount is less than £50:
# If the user has a Premium Membership, the delivery fee is £3.
# If the user does NOT have a Premium Membership, the delivery fee is £7.
# Hint variables to use:
# amount (e.g., 55 or 30)
# is_premium (e.g., True or False)
                                    
                  #_________________SOLUTION________________#
Shopping_Amount = int(input("Enter the amount of shopping:"))
is_premium = bool(input("is your account is premium (yes/no) :"))
if(Shopping_Amount>=50):
    print("your amount is more than 50")
    if(is_premium =="yes") :
        print("If the user has a Premium Membership, the delivery is Free (£0).")

    elif(is_premium == "no"):
         print("If the user does NOT have a Premium Membership, the delivery fee is £2.")

elif(Shopping_Amount<50):
    print("your ammount is less than 50")
    if(is_premium == "yes") :
        print(" the delivery fee is £3.")
    elif(is_premium == "no"):
        print("the delivery fee is £7")

            #_____________(special note)_____________ 
    #if you have any query about my program then you can ask me in comment 
    #And you find any mistake in my program then tell me in comment it is very helpfull  for me.





    



