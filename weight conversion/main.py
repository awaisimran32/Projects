weight = float(input("Enter your weight : "))
unit=input("you want it in Kilograms or pounds? (K or l) : ")
if unit== "k":
    kilo=weight/2.20
    unit="kgs"
    print(f"your weight in KG is {round(kilo)}{unit}")
elif unit=="l":
    unit="Lbs"
    pound=weight*2.20
    print(f"your weight in Lbs is {round(pound)}{unit}")
else:
    print(f"{unit} is not valid.")







