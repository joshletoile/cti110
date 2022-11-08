#CTI-110
#P4HW1 - Score List
#Joshua Letoile
#11/8/2022

#---------Pseudocode---------
#Ask user how many scores they want to enter.
#Increment for loop amount of times user entered.
#Prompt user for score for every loop the for loop does and enter scores into a list.
#Store grades in a list with a descriptive name.
#If score is not between 0 and 100 reprompt the user to enter a valid score.
#Print lowest grade in the list.
#Remove lowest grade from list and then find the average grade of list.
#Print Modified List and Scores Average below that.
#Lastly, print the final grade using a while loop and a if else statement that increments through the
#possible letter grades based on average grade.
#-----------------------------

amt_of_scores = int(input("How many scores do you want enter? "))
print()
score = 0
module_grades = []
for i in range(amt_of_scores):
    increment = i + 1
    score = float(input("Enter score #" + str(increment) + ": "))
    if score >= 0 and score <= 100:
        module_grades.append(score) 
    else:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score #" + str(increment) + " again: "))
        module_grades.append(score)

print()
print()
print("------------Results------------")
print("Lowest Grade  :", f"{min(module_grades):>1}")
module_grades.remove(min(module_grades))
average_grade = sum(module_grades) / len(module_grades)
print("Modified List :", module_grades)
print("Scores Average:", f"{average_grade:.2f}")

boolean = True
while boolean == True:
    if average_grade >= 90 and average_grade <=100:
        print("Grade         :", "A")
        boolean = False
    elif average_grade >= 80 and average_grade <90:
        print("Grade         :", "B")
        boolean = False
    elif average_grade >= 70 and average_grade <80:
        print("Grade         :", "C")
        boolean = False
    elif average_grade >= 60 and average_grade <70:
        print("Grade         :", "D")
        boolean = False
    else:
        print("Grade         :", "F")
        boolean = False

print("-----------------------------------------")
