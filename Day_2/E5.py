# Height

height1 = int(input("What is your height: "))

can_ride = False

if height1 >= 120:
    can_ride = True

if can_ride:
   age = int(input("How old are you: ")) 

   bill = 0

   if age < 12:
       bill += 5
   elif age > 12 and age <= 18:
       bill += 7
   elif age > 18 and age <= 45:
       bill += 9

   if input("Do you want a photo (s/n)").lower()  == 's':
       bill += 3
     
   print(f"You have to pay {bill}")
   

else:
    print("Can't ride")


 
