print("Welcome to the tip Calculator !")
bill=float(input("what was the total bill ? $ "))
tip=float(input("what percentage tip would you like to give ? 10,12 or 15 ? "))
person=int(input("How many people to split the bill ? "))
total_bill=tip /100 * bill +bill
per_person=total_bill/person
total=round(per_person , 2)
print(f"Each person should pay : $ {total}")
