#Travel expenses calculator
#9/15/2022
#CTI-110 P1HW2 - Travel Expense
#Joshua Letoile
#

#Program Pseudocode
#Display or print program description.
#Have user input budget, destination, gas, accomodation, and food
#with each number being specified as a float.
#Display or print all expenses with proper description of each for the user. ie Fuel for gas,
#or Initial Budget for budget.
#Lastly, calculate remaining balance by subtracting total expenses from initial total budget.


print("This program calculates and displays travel expenses\n")

budget = float(input("Enter budget: "))
print("")
destination = input("Enter your travel destination: ")
print("")
gas = float(input("How much do you think you will spend on gas? "))
print("")
accomodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
print("")
food = float(input("Last, how much do you need for food? "))
print("")

print("------------Travel Expenses------------")
print("Location:", destination)
print("Initial budget:", budget)
print("")
print("Fuel:", gas)
print("Accomodation:", accomodation)
print("Food:", food)
print("")
print("Remaining balance:", budget - (gas + accomodation + food))
