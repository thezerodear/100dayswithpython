print("welcome to the share pay calculator!")
bill = float(input("What was the total bill? $"))
if bill <= 0:
    print("Please enter a valid bill amount.")
    exit()
percent = int(input("How much service charge this restaurant charge? enter only the number"))
people = int(input("How many people to split the bill?"))
if people <= 0:
    print("if you want to split the bill, please enter a valid number of people.")
    exit()
print("Each person should pay: $" + str(round(bill * (1+percent/100)/people)))