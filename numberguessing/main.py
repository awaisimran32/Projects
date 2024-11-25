import random
lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
guesses=0
is_running=True


print("-----------GUESS GAME-------------")
print(f"Guess The Number between {lowest_num} and {highest_num}")

while is_running:
    guess=input("Enter Your Guess : ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess<lowest_num or guess>highest_num:
            print("Number you gave is out of Range.")
        elif guess<answer:
            print("Increase The Number!")
        elif guess>answer:
            print("Decrease The Number!")
        else:
            print(f"The Correct Answer is {answer}. ")
            print("----------------------------------")
            print("-------------YOU WON--------------")
            print("----------------------------------")
            print(f"Number of guesses: {guesses}")
            is_running=False
    else:
        print("Invalid guess")
        print(f"Give a Number between {lowest_num} and {highest_num}")