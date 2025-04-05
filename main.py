#Prompt user to display the change owed
change = float(input("Enter change owed (in $, not cents!!): "))

#Convert the change into an integer (i.e $0.25 becomes 25 cents)
change = change * 100

array_changes = [5, 10, 15, 20]
arr_size = len(array_changes)

array = [0, 1, 2, 3, 4]
length = len(array)



#WHen change owed is a nickel, dime or quarter
if change == 5 or change == 10 or change == 25:
    number = 1
    amount = 1
    print(f"\nNumber of coins to carry: {number} \nBreakdown:  {int(change)} cents * {amount}\n")

#when change is under a nickel
if change in range(5):
    number = int(change)
    amount = int(change)
    print(f"\nYou will carry: {number} coins \n\nTotal breakdown: 1 cent * {amount}\n")

#when change is between 5 and 15
if change in range(5,25,1):
    for i in range(arr_size):
        for j in range(length):
            if change - array[j] == array_changes[i]:
                if array_changes[i] == 15:
                    #number of coins to carry
                    number = array[j] + 2
                    print(f"\nYou will carry: {number} coins\n")
                    # total breakdown
                    if array[j] == 0:
                        print(f"Total breakdown: {array_changes[1]} cents * 1, {array_changes[0]} cents * 1 \n")
                    else:
                        print(f"Total breakdown: {array_changes[1]} cents * 1, {array_changes[0]} cents * 1, 1 cent * {array[j]} \n")
                elif array_changes == 20:
                    #number of coins to carry
                    number = array[j] + 2
                    print(f"\nYou will carry: {number} coins\n")
                    # total breakdown
                    if array[j] == 0:
                        print(f"Total breakdown: {array_changes[1]} cents * 2\n")
                    else:
                        print(f"Total breakdown: {array_changes[1]} cents * 2, {array_changes[0]} cents * 1, 1 cent * {array[j]} \n")
                else:

                    #number of coins to carry
                    number = array[j] + 1
                    print(f"\nYou will carry: {number} coins\n")
                    #  total breakdown
                    if array[j] == 0:
                        print(f"Total breakdown: {array_changes[i]} cents * 1")
                    else:
                        print(f"Total breakdown: {array_changes[i]} cents * 1, 1 cent * {array[j]} \n")
