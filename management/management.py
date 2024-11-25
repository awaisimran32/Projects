print("Welcome To My cafe")
Menu={
    'hot coffee':80,
    'cold coffee':200,
    'chocolate shake':250,
    'tea':50,
    'special tea':80
}
print("Hot Coffee:80\nCold Coffee:200\nChocolate Shake:250\nTEA:50\nSpecial TEA:80")

order_total=0
n=str(input("What Would you like to order :) "))

if n.lower() in Menu:
    order_total+=Menu[n]
    print(f"your {n} is on its way ")
    print(f"Your total is {order_total}")
else:
    print("Sorry! But We do not have this.")