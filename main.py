print('''
                                                             
                                 ad88    ad88 88             
                                d8"     d8"   88             
                                88      88    88             
8b      db      d8 ,adPPYYba, MM88MMM MM88MMM 88  ,adPPYba,  
`8b    d88b    d8' ""     `Y8   88      88    88 a8P_____88  
 `8b  d8'`8b  d8'  ,adPPPPP88   88      88    88 8PP"""""""  
  `8bd8'  `8bd8'   88,    ,88   88      88    88 "8b,   ,aa  
    YP      YP     `"8bbdP"Y8   88      88    88  `"Ybbd8"'  
                                                             
                                                             
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#Write your code below this line 👇
ch1 = input ("You'r at a cross road. Where do you go: Left or Right")
if ch1 == "Left":
  ch2 = input ("swim or wait")
  if ch2 == "wait":
    ch3 = input ("which door: red, blue, yellow")
    if ch3 == "yellow":
          print ("YOU WIN BROOO!!!")
    elif ch3 == "red":
          print ("YOU BURN. GAME OVER") 
    elif ch3 == "blue":
          print ("EATEN BY BEAST.GAME OVER")
    else :
          print ("GAME OVER")
  else:
    print ("ATTACKED BY TROUT.GAME OVER")

else:
  print ("FALL INTO HALL. GAME OVER")