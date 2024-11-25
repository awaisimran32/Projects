import random
options=("rock","paper","scissors")


playing=True


while playing:
    
    player=None
    computer=random.choice(options)





    while player not in options:
        player = input("Enter a choice (rock, paper, scissors) : ")
    

    print(f"Player:{player}")
    print(f"Computer:{computer}")


    if player==computer:
        print("It's a TIE ! ")
    elif player=="rock" and computer=="scissors":
        print("------------- YOU WON -----------")
    elif player=="scissors" and computer=="paper":
        print("---------------YOU WON-------------------")
    elif player=="paper" and computer=="rock":
        print("-------------YOU WON----------------")
    elif player=="scissors" and computer=="rock":
        print("-------------YOU LOSE----------------")
    elif player=="paper" and computer=="scissors":
        print("-------------YOU LOSE----------------")
    elif player=="rock" and computer=="paper":
        print("-------------YOU LOSE----------------")
    play_again=input("Play Again(y/n) : ").lower()
    if not play_again=="y":
        playing=False
print("Thanks For Playing")        
