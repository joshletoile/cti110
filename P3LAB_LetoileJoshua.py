is_leap_year = False
   
input_year = int(input())

if (input_year / 4) % 4 == 0:
    is_leap_year = True
    print(input_year, "- leap year")
else:
    print(input_year, "- not a leap year")
