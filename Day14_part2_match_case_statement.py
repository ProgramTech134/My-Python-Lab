# __________________________________________________________________________________________________________
# |___|______|______|________|_______|____Program Statement: ATM Menu System___|____|____|_____|______|____|
# |__|_____|_____|______|_________|_________|_______|______|_____|_____|______|________|________|______|___|
# Create a simple ATM program. Take an option number (an integer) as input from the user. Use a match-case statement to perform these actions:

# If the input is 1, print: "Your current balance is $5,000."

# If the input is 2, print: "Please insert your cash to deposit."

# If the input is 3, print: "Please enter the amount you want to withdraw."

# If the input is 4, print: "Thank you for using our ATM. Goodbye!"

# If the input is anything else (Default case), print: "Invalid option! Please choose a number between 1 and 4
   
check_status = int(input("Enter the integer from 1 to 4"))


match check_status :

    case 1 :
      print("Your current balance is $5,000.")
    case 2 :
      print("Please insert your cash to deposit.")
    case 3 :
      print("Please enter the amount you want to withdraw.")
    case 4 :
      print("Thank you for using our ATM. Goodbye!")

    case _:
      print("Invalid option! Please choose a number between 1 and 4.")


