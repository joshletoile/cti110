#CTI-110
#P2HW2 - List
#Joshua Letoile
#10/4/2022

#Create 6 input variables prompting user for 6 module grades.
#Store grades in a list with a descriptive name.
#Calculate average grade and store it in a variable.
#Print results in a neatly formatted Results section that includes
#the lowest grade, highest grade, sum of grades, and average grade.

mod1_grade = float(input("Enter grade for Module 1: "))
mod2_grade = float(input("Enter grade for Module 2: "))
mod3_grade = float(input("Enter grade for Module 3: "))
mod4_grade = float(input("Enter grade for Module 4: "))
mod5_grade = float(input("Enter grade for Module 5: "))
mod6_grade = float(input("Enter grade for Module 6: "))

module_grades = [mod1_grade, mod2_grade, mod3_grade, mod4_grade, mod5_grade, mod6_grade]

average_grade = sum(module_grades) / len(module_grades)

print("------------Results------------")
print("Lowest Grade:", f"{min(module_grades):>10}")
print("Highest Grade:", f"{max(module_grades):>9}")
print("Sum of Grades:", f"{sum(module_grades):>10}")
print("Average:           ", f"{average_grade:.2f}")
print("-----------------------------------------")
