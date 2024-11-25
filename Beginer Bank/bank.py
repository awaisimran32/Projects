def show_balance(balance):
    print(f"You Balance is {balance}$")

def deposit():
    amount=float(input("How Much money would you like to deposit : "))

    if amount<0:
        print("That's not valid.")
        return 0
    else:
        return amount


def withdraw(balance):
    amount=float(input("How Much money would you like to withdraw : "))
    if amount>balance:
        print("You dont have enough funds")
        return 0
    elif amount <0:
        print("Amount should be greater than zero.")
        return 0
    else:
        return amount
def main():

    balance=0
    is_running=True

    while is_running:
        print("1.Show Balance")
        print("2.Deposit")
        print("3.withdraw")
        print("4.Exit")
        choice=input("Give your Choice : ")
        if choice=='1':
            show_balance(balance)
        elif choice =='2':
            balance+=deposit()
        elif choice=='3':
            balance-=withdraw(balance)
        elif choice=='4':
            is_running=False
        else:
            print("This is not a valid Choice.")

if __name__ =='__main__':
    main()


