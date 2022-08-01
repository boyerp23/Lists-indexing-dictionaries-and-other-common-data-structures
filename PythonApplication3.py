#File creator: Paul Boyer
#pauboyer@uat.edu
#CSC235 Python Programming 1
#WK 1 assignment 3


# Information that we will call to print out
intro = "This is my chicken paramasian receipe\n"#+\
    #"It requires the following:\n 1. Chicken\n 2. Sauce\n 3.Breading\n 4.Pasta\n"
# Steps for completing the program instruction
s1 = 'a'
s1 = f's{1} Flatten Chicken\n'
s2 = f's{2} Add breading to chicken\n'
s3 = f's{3} Cook chicken in pan with light olive oil\n'
s4 = f's{4} Boil pasta and cook sauce\n'
s5 = f's{5} Bring it all together\n'

# Calling the print function to display information 
print(intro)
#a tuple is a collection which is ordered and unchangable. Allows for duplicates.
#order will remain the same each time
myIngrediantTuple = ("Chicken", "Sauce", "Breading", "Pasta", "Red Pepper")
#prints out the number of items in 'mytuple'
print(len(myIngrediantTuple))
print("ingrediants are needed for this recipe."+\
    " They are listed as:")
#prints out the list of ingrediants found in 'mytuple'
print(myIngrediantTuple)
#set is a collection which is unordered, unchangeable (but can be removed and new items added), and unindexed. No duplicate members.
#order is ramdom each time.
myEquipmentSet = set(("2 quart pot", "Stirring Spoon", "Oven Mit", "Ladel", "Serving Dishes and Silverware", "Serving Spoon"))
#prints 'myEquipmentSet' in no particular order each time and ignores duplicated memebers - "Serving Spoon"
print(myEquipmentSet)
print("Is the equipment needed in order to prepare and serve dish\n")
print(s1)
# Ask for user input
print ("Do you like spicy food? enter 'Y' for yes\n")
# Input function with y / n varible that will be called in IF statement 
y_n = input()
# If user input = 'y' program will execute steps within if statement and through the rest of the program
if y_n == 'y':
    # Ask user for input
    print("How spicy do you like your breading? 1-5\n")
    # Ask user to input a numerical value for their input - no rule exists to prevent any input from being accepted at this time.
    spice_lvl = input()
    # If 'y' is input then following user input the this will be output to the display to match user input and statement
    print(f's{2} Add breading to chicken\n and add crushed red peppers to match spice level {spice_lvl}\n')
# If user input = 'n' statement will print as written in step 2 and through the rest of the program  
else:
    print(s2) 
# Calling the print function to display information        
print(s3)
# Ask for user input 
print("Do you prefer sauce in jar? enter 'y' for yes\n")
# Input function with y / n varible that will be called in IF statement 
y_n = input()
# If user input = 'y' program will execute steps within if statement and through the rest of the program
if y_n == 'y':
    # Ask for user input
    print ("what sauce do you use?\n")
    # Ask user for what type of sauce they prefer if they don't want to make their own. EX Ragu or Prego
    sauce_input = input()
    # If 'y' is input then following user input the this will be output to the display to match user input and statement
    print(f's{4} Boil pasta and add {sauce_input} to your pasta')
# If user input = 'n' statement will print as written in step 2 and through the rest of the program  
else:
    print(s4)
print(s5)
#a collection which is ordered and unchangable. Allows duplicate members

