#Prompt user to display the change owed
change = float(input("Enter change owed: "))

#Convert the change into an integer (i.e $0.25 becomes 25 cents)
change = change * 100



#WHen change owed is a nickel, dime or quarter
if change == 5 or change == 10 or change == 25:
    number = 1
    amount = 1
    print(f"\nNumber of coins to carry: {number} \nBreakdown:  {change} cents * {amount}\n")

#when change is under a nickel
if change in range(5):
    number = int(change)
    amount = int(change)
    print(f"\nYou will carry: {number} coins \n\nTotal breakdown: 1 cent * {amount}\n")
