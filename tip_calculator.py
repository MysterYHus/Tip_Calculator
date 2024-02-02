bill = float(input("What was the total bill: "))
tip = int(input("What percentage tip would you like to give? "))
group_size = int(input("How many people should split the bill? "))
tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
share = round(total_bill / group_size, 2)



print("Each person should pay:", share)


