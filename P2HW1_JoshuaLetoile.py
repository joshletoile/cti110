#Travel expenses calculator
#9/27/2022
#CTI-110 P2HW1 - Travel 
#Joshua Letoile
#

#Program Pseudocode
#Display or print program description.
#Have user input budget, destination, gas, accomodation, and food
#with each number being specified as a float.
#Utilize dollar sign variable in formatting the expenses.
#Display or print all expenses with proper description of each for the user. ie Fuel for gas,
#or Initial Budget for budget.
#Also properly align each of the expenses and format them as strings.
#Lastly, calculate remaining balance by subtracting total expenses from initial total budget.


print("This program calculates and displays travel expenses\n")

budget = float(input("Enter Budget: "))
print("")
destination = input("Enter your travel destination: ")
print("")
gas = float(input("How much do you think you will spend on gas? "))
print("")
accomodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
print("")
food = float(input("Last, how much do you need for food? "))
print("")
dollar_symbol = "$"

print("------------Travel Expenses------------")
print("Location:", f"{destination:>19}")
print("Initial budget:", f"{dollar_symbol:>5}{budget:>6}")
print("Fuel:", f"{dollar_symbol:>15}{gas:>5}")
print("Accomodation:", f"{dollar_symbol:>7}{accomodation:>5}")
print("Food:", f"{dollar_symbol:>15}{food:>5}")
print("----------------------------------------")
print("")
print("Remaining balance:", " $" + str(budget - (gas + accomodation + food)))
