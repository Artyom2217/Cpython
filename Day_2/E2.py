#it's a leap year

year1 = int(input("Type a year: "))
Is_leap = False

"""if year1 % 4 == 0:
    if year1 % 100 == 0:
        if year % 400 == 0:
            Is_leap = True
            
    elif year1 % 100 != 0:
        Is_leap = True"""

if year1 % 4 == 0 and year1 % 100 == 0 and year1 % 4 == 400:
    Is_leap = True
elif year1 % 4 == 0 and year1 % 100 != 0:
    Is_leap = True


if Is_leap: 
    print(f"{year1} it's a leap year")
elif not Is_leap:
    print("it's not a leap year")

