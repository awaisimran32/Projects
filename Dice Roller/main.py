import random
# print("\u25cf \u250c \u2500 \u2510 \u2502 \u2514 \u2518 ")
# ● ┌ ─ ┐ │ └ ┘ 
#  
diceart={
    1:( "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2:( "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    3:( "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4:( "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5:( "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),                        
    6:( "┌─────────┐",
        "│ ●  ●  ● │",
        "│         │",
        "│ ●  ●  ● │",
        "└─────────┘")
}
dice=[]
total=0
num_of_dice=int(input("How Many Dices you want to spin? : "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

# for die in range(num_of_dice):
#     for line in diceart.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print(diceart.get(die)[line],end="")
    print()





for die in dice:
    total+= die
print(f"Total:{total}")

# WHat is Happening?