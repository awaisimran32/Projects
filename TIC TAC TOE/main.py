
def printboard():
    print(f" 0 | 1 | 2 ")
    print( "---|---|---")
    print(f" 3 | 4 | 5 ")
    print( "---|---|---")
    print(f" 6 | 7 | 8 ")
    print( "---|---|---")





if __name__ == "__main__":
    xstate = [0,0,0,0,0,0,0,0,0]
    zstate = [0,0,0,0,0,0,0,0,0]
    turn = 1 
    print("Welcome to TIC TAC TOE")
    while (True):
        printboard(xstate,zstate)
        if(turn==1):
            print("X's Chance")
            value = int(input("Please enter a value"))
            xstate[value]=1
        else:
            print("X's Chance")
            value = int(input("Please enter a value"))
            zstate[value]=1

        break
