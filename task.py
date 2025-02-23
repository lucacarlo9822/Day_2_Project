print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


Total = bill * (tip / 100) + bill
price_per_person = Total / people

final_price = round(price_per_person,2)

print(f"Your total is {final_price} per person")

