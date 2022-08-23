# Write your code below this line 👇
height = input("Please enter your height in cm\n")
heighti = int(height)

#if lookup buradan sonra basliyor

if heighti >= 120:
  print("you can use the rollercoster")
  age = input("Please enter your age\n")
  agei = int(age)
  if agei >= 18:
    bill = 12
  elif agei >= 12:
    bill = 7
  else: 
    bill = 5

  photo = input("do you want photo taken? Y or N ?")
  if photo == "Y":
    bill += 3
    print(f"please pay ${bill}")

  else :
    print(f"please pay ${bill}")
else: 
  print("you cannot write - you are too short")