num1= input("Type a number: ")

Is_even = False
Is_eight = False

if int(num1) % 2 == 0:
    num1 = int(num1)
    Is_even = True
    if num1 == 8:
        Is_eight = True

if Is_even == True:
    print(f"{num1} is even")
    if Is_eight:
        print("num1 = 8")
elif not Is_even:
    print(f"{num1} is add")
