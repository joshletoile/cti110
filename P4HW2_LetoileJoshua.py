#CTI-110
#P4HW2 - Salary Calculator
#Joshua Letoile
#11/8/2022

#-------PSEUDOCODE--------
#Prompt user for employee name, employee pay rate, and hours worked.
#Calculate overtime pay and regular hour pay and create variables for these.
#Print Employee name, hours worked, pay rate, overtime, overtime pay, regular hour pay, and gross pay.
#Loop this until the user enters None for name.
#Create variables collecting total number of employees, total amount payed for OT, total amount payed for reg hours, and total gross
#as the loop iterates.
#At the end of the program print total number of employees entered, total amount payed for overtime,
#total amount payed for regular hours, and total amount payed in gross.
#PROGRAM MAY UTILIZE WHILE LOOP AND IF ELSE STATEMENTS FOR CONDITIONS SUCH AS OVERTIME HOURS VS REGULAR HOURS
#-------------------------

name = ""
employee_count = 0
overtime_total = 0
regpay_total = 0
while True:
    name = input('Enter employee\'s name or "None" to terminate: ')
    if name == str(None):
        break
    hours = float(input("How many hours did " + name + " worked? "))
    pay_rate = float(input("What is " + name + "'s pay rate? "))
    overtime_hours = 0
    overtime_pay = 0
    employee_count += 1

    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        overtime_total += overtime_pay

    if hours > 40:
        hours = 40
    else:
        hours = hours

    regular_pay = hours * pay_rate
    regpay_total += regular_pay
    total_pay = regular_pay + overtime_pay
    regular_pay = "$" + (f"{regular_pay:.2f}")
    total_pay = "$" + (f"{total_pay:.2f}")

    print()
    print("Employee name:  ", name)
    print("")
    print("Hours Worked   Pay Rate    Overtime    Overtime Pay        RegHour Pay         Gross Pay")
    print("--------------------------------------------------------------------------------------------------")
    print(f"{hours :<14}", f"{pay_rate:<11}", f"{overtime_hours:<11}", f"{overtime_pay:<19}", f"{regular_pay:<19}", f"{total_pay:<20}")
    print()
    print()

print()
print("Total number of employees entered:" + str(employee_count))
print("Total amount payed for overtime: $" + f"{overtime_total:.2f}")
print("Total amount payed for regular hours: $" + f"{regpay_total:.2f}")
print("Total amount payed in gross: $" + f"{regpay_total + overtime_total:.2f}")
