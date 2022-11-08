#CTI-110
#P3HW2 - Salary
#Joshua Letoile
#10/20/2022
#Program computing total pay based on hours worked both overtime and regular.

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
overtime_hours = 0
overtime_pay = 0

if hours > 40:
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * pay_rate * 1.5

regular_pay = 40 * pay_rate
total_pay = regular_pay + overtime_pay
regular_pay = "$" + (f"{regular_pay:.2f}")
total_pay = "$" + str(total_pay)

print("-------------------------------------")
print("Employee name:  ", name)
print("")
print("Hours Worked   Pay Rate    Overtime    Overtime Pay        RegHour Pay         Gross Pay")
print("--------------------------------------------------------------------------------------------------")
print(f"{hours :<14}", f"{pay_rate:<11}", f"{overtime_hours:<11}", f"{overtime_pay:<19}", f"{regular_pay:<19}", f"{total_pay:<20}")
