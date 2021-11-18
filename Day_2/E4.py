#FizzBuzz

Num = int(input("Type a number: "))

Is_FizzBuzz = False
Is_Fizz = False
Is_Buzz = False

if Num % 3 == 0 and Num % 5 == 0:
    Is_FizzBuzz = True
elif Num % 3:
    Is_Fizz = True
elif Num % 5:
    Is_Buzz = True


if Is_FizzBuzz: 
    print(f"{Num} FizzBuzz")
elif not Is_Fizz:
    print(f"{Num} Fizz")
elif not Is_Buzz:
    print(f"{Num} Buzz")
else:
    print("None")