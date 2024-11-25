unit=input("Is temperature celsius or farhenit (c/f) : ")
temp=float(input("Tell the temprature:"))
if unit=="c":
# in celsius convert to F
    temp=round((9*temp)/5+32,1)
    print(f"The temp in farhenit is {temp}")
elif unit=="f":
    temp=round((temp-32)*5/9,1)
    print(f"The temp in celsius is {temp}")
    # in farhenit convert to c
else:
    print("Wrong unit")