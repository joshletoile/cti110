#Math Quiz
#11/22/2022
#CTI-110-P5HW2 - Math Quiz
#Joshua Letoile
import random

print("Welcome to Math Quiz")
print()
print()

def main_menu():
    print("MAIN MENU")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()
    
def too_low():
    print("Sorry, guess is too low.")
    print()
    print("try again: ", end="")
    
def too_high():
    print("Sorry, guess is too high.")
    print()
    print("try again: ", end="")

def correct():
    print("Congradulations!!!! your answer is correct..")
    
def add(a,b):
    #a = random.randint(0, 100)
    #b = random.randint(0, 100)
    print("  " + str(a))
    print("+ " + str(b))
    print()
    print("Enter answer.")
    user_answer = int(input())
    i = 1
    while user_answer != (a+b):
        if user_answer < (a+b):
            i += 1
            too_low()
            user_answer = int(input())
        elif user_answer > (a+b):
            i += 1
            too_high()
            user_answer = int(input())
            
    correct()
    print("Number of guesses: " + str(i))

        
def subtract(a,b):
##    a = random.randint(0, 100)
##    b = random.randint(0, 100)
    print("  " + str(a))
    print("- " + str(b))
    print()
    print("Enter answer.")
    user_answer = int(input())
    i = 1
    while user_answer != (a-b):
        if user_answer < (a-b):
            i += 1
            too_low()
            user_answer = int(input())
        elif user_answer > (a-b):
            i += 1
            too_high()
            user_answer = int(input())
            
    correct()
    print("Number of guesses: " + str(i))  
        
def user_option():
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    if user_input == 1:
        add(a,b)
    elif user_input == 2:
        subtract(a,b)
    else:
        print("Invalid input, enter a number from 1-3.")

if __name__ == '__main__':
    main_menu()
    user_input = int(input("Please choose one of the menu options: "))
    while user_input != 3:
        user_option()
        print()
        main_menu()
        user_input = int(input("Please choose one of the menu options: "))
        
    print("Thank you for playing...")
    print("Bye!!")
    
