#it's a leap year

year1 = input("Type a year: ")

if int(year1) % 4 == 0:
    year1 = int(year1)
    print(f"{year1} it's a leap year")
elif int(year1) % 4 != 0:
    year1 = int(year1)
    print(f"{year1} it's not a leap year")
else:
    print("Invalid date")