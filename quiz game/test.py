questions = (
    "How many elements in the periodic table? :",
    "Which animal lays the largest eggs? :",
    "What is the most abundant gas in earth's atmosphere? :",
    "How many bones are in the human body?:",
    "Which planet in the solar system is the hottest?:",
    "What is the chemical symbol for water?:",
    "Which planet is known as the Red Planet?:",
    "Which element is needed for strong bones?:",
    "Who developed the theory of relativity?:",
    "What is the hardest natural substance on Earth?:",
    "How long does it take for the Earth to orbit the Sun?:",
    "What is the largest mammal?:",
    "Which gas is used in balloons to make them float?:",
    "How many teeth does an adult human have?:",
    "Which organ is responsible for pumping blood in the human body?:",
    "Which organ in the body produces insulin?:",
    "What is the boiling point of water at sea level in Celsius?:",
    "Which planet is closest to the Sun?:",
    "How many legs do spiders have?:",
    "Which metal is liquid at room temperature?:",
    "Which planet is known for its rings?:",
    "How many planets are in the solar system?:",
    "Which scientist discovered penicillin?:",
    "Which element has the atomic number 1?:",
    "What is the smallest unit of life?:"
)

options = (
    ("A.116", "B.117", "C.118", "D.119"),
    ("A.whale", "B.Crocodile", "C.Elephant", "D.Ostrich"),
    ("A.Nitrogen", "B.Oxygen", "C.Carbon", "D.Hydrogen"),
    ("A.206", "B.209", "C.300", "D.250"),
    ("A.Mercury", "B.Venus", "C.Earth", "D.Mars"),
    ("A.H2", "B.WA", "C.HO", "D.H2O"),
    ("A.Jupiter", "B.Venus", "C.Mars", "D.Mercury"),
    ("A.Iron", "B.Calcium", "C.Carbon", "D.Hydrogen"),
    ("A.Newton", "B.Darwin", "C.Einstein", "D.Tesla"),
    ("A.Diamond", "B.Iron", "C.Gold", "D.Silver"),
    ("A.24 hours", "B.30 days", "C.365 days", "D.7 days"),
    ("A.Elephant", "B.Whale", "C.Giraffe", "D.Shark"),
    ("A.Oxygen", "B.Helium", "C.Carbon dioxide", "D.Hydrogen"),
    ("A.20", "B.28", "C.32", "D.35"),
    ("A.Brain", "B.Lungs", "C.Heart", "D.Kidneys"),
    ("A.Pancreas", "B.Liver", "C.Heart", "D.Lungs"),
    ("A.50°C", "B.75°C", "C.100°C", "D.150°C"),
    ("A.Venus", "B.Earth", "C.Mercury", "D.Mars"),
    ("A.6", "B.8", "C.10", "D.12"),
    ("A.Lead", "B.Iron", "C.Mercury", "D.Gold"),
    ("A.Jupiter", "B.Mars", "C.Saturn", "D.Uranus"),
    ("A.6", "B.7", "C.8", "D.9"),
    ("A.Newton", "B.Pasteur", "C.Fleming", "D.Tesla"),
    ("A.Oxygen", "B.Hydrogen", "C.Helium", "D.Carbon"),
    ("A.Atom", "B.Molecule", "C.Cell", "D.Tissue")
)

answers = (
    "C", "D", "A", "A", "B", 
    "D", "C", "B", "C", "A", 
    "C", "B", "B", "C", "C", 
    "A", "C", "C", "B", "C", 
    "C", "C", "B", "C", "C"
)

guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")
    
    question_num += 1

print("------------------------------")
print("            Results           ")
print("------------------------------")
print("Answers : ", end="")
for answer in answers:
    print(answer, end="")
print()

print("Your guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()

print(f"Your score is {score}/{len(questions)}")
