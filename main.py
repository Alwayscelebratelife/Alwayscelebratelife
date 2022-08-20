# Write your code below this line 👇
print("Welcome to Tip calculator")
bill = input("Please enter total bill value\n")
tip = input("Please enter desired tip rate, suggestions: 15%, 20%, 25%\n")
size = input ("what is the size of your party?\n")

billx = float(bill)
tipx = float (tip)
sizex = float (size)


per_value = (billx + billx * (tipx / 100)) / sizex

per_valuex = round(per_value,2)

print("each person needs to pay" ,per_valuex, "$")
