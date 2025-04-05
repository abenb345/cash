#Prompt user to display the change owed
price = float(input("Enter price of item: "))

cash = float(input("Enter how much cash you are giving: "))

change = cash - price
#Convert the change into an integer (i.e $0.25 becomes 25 cents)
change = change * 100

#declare multiple variables to know how many of each cents are required to equate the change
quarter_multiples = int(change/25)
quarter_remainder = int(change % 25)

dime_multiples = int(change/10)
dime_remainder = int(change % 10)

nickel_multiple = int(change/5)
nickel_remainder = int(change % 5)


#for change larger than 24 cents
if quarter_multiples > 0:
    if quarter_remainder == 0:
        print(f"You will carry {quarter_multiples} coins")
        print(f"Total breakdown: 25 cents * {quarter_multiples}")
    elif quarter_remainder in range(1,5,1):
        number = quarter_multiples + quarter_remainder
        print(f"You will carry {number} coins")
        print(f"Total breakdown: 25 cents * {quarter_multiples}, 1 cent * {quarter_remainder}")
    elif quarter_remainder == 5 or quarter_remainder == 10:
        number = quarter_multiples + 1
        print(f"You will carry {number} coins")
        print(f"Total breakdown: 25 cents * {quarter_multiples}, {quarter_remainder} cents * 1")
    elif quarter_remainder in range(6,15,1):
        if quarter_remainder in range(10, 15,1):
            number = quarter_multiples + (quarter_remainder - 10) + 1
            print(f"You will carry {number} coins")
            if quarter_remainder - 10 != 0:
                print(f"Total breakdown: 25 cents * {quarter_multiples}, 10 cents * 1, 1 cent * {quarter_remainder - 10}")
            else:
                print(f"Total breakdown: 25 cents * {quarter_multiples}, 10 cents * 1")
        else:
            number = quarter_multiples + 1 + (quarter_remainder - 5)
            print(f"You will carry {number} coins")
            print(f"Total breakdown: 25 cents * {quarter_multiples}, 5 cents * 1, 1 cent * {quarter_remainder - 5}")
    elif quarter_remainder in range(15, 20, 1):
        number = quarter_multiples + 2 + (quarter_remainder - 15)
        print(f"You will carry {number} coins")
        if quarter_remainder - 15 != 0:
            print(f"Total breakdown: 25 cents * {quarter_multiples}, 10 cents * 1, 5 cents * 1, 1 cent * {quarter_remainder - 15}")
        else:
            print(f"Total breakdown: 25 cents * {quarter_multiples}, 10 cents * 1, 5 cents * 1")
    elif quarter_remainder in range(20, 25, 1):
        number = quarter_multiples + 2 + (quarter_remainder - 20)
        print(f"You will carry {number} coins")
        if quarter_remainder - 20 != 0:
            print(f"Total breakdown: 25 cents * {quarter_multiples}, 10 cents * 2, 1 cent * {quarter_remainder - 20}")
        else:
            print(f"Total breakdown: 25 cents * {quarter_multiples}, 10 cents * 2")

# for change between 10 and 24 cents ncluded
elif dime_multiples > 0:
    if dime_remainder == 0:
        print(f"You will carry {dime_multiples} coins")
        print(f"Total breakdown: 10 cents * {dime_multiples}")
    elif dime_remainder in range(1,5,1):
        number = dime_multiples + dime_remainder
        print(f"You will carry {number} coins")
        print(f"Total breakdown: 10 cents * {dime_multiples}, 1 cent * {dime_remainder}")
    elif dime_remainder == 5:
        number = dime_multiples + 1
        print(f"You will carry {number} coins")
        print(f"Total breakdown: 10 cents * {dime_multiples}, {dime_remainder} cents * 1")
    elif dime_remainder in range(6,10,1):
        number = dime_multiples + 1 + (dime_remainder - 5)
        print(f"You will carry {number} coins")
        print(f"Total breakdown: 10 cents * {dime_multiples}, 5 cents * 1, 1 cent * {dime_remainder - 5}")

#for change between 6 and 9 cents included
elif nickel_multiple > 0:
    if nickel_remainder == 0:
        print(f"You will carry {nickel_multiple} coins")
        print(f"Total breakdown: 5 cents * {nickel_multiple}")
    elif nickel_remainder in range(1,5,1):
        number = nickel_multiple + nickel_remainder
        print(f"You will carry {number} coins")
        print(f"Total breakdown: 5 cents * {nickel_remainder}, 1 cent * {nickel_remainder}")

#for change less than 6 cents
else:
    print(f"You will carry {change} coins")
    print(f"Total breakdown: 1 cent * {change}")
