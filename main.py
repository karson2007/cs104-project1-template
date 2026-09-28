# Basketball Quiz
# Author: Karson Knight
# A quiz/questionnaire program built for CS 104 Project 1

score = 0

print("Welcome to the Basketball Quiz!")
print("Choose the correct answer for each question.")

answer1 = input("Who has the most NBA championships as a player?\n1. Bill Russell\n2. Michael Jordan\n3. LeBron James\n")
if answer1 == "1":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect. The answer is Bill Russell.")

answer2 = input("How many points is a three-pointer worth?\n1. 1 point\n2. 2 points\n3. 3 points\n")
if answer2 == "3":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect. A three-pointer is worth 3 points.")

answer3 = input("Which team does Stephen Curry play for?\n1. Los Angeles Lakers\n2. Golden State Warriors\n3. Boston Celtics\n")
if answer3 == "2":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect. Stephen Curry plays for the Golden State Warriors.")

answer4 = input("How many players from one team are on the court at one time?\n1. 5 players\n2. 6 players\n3. 7 players\n")
if answer4 == "1":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect. There are 5 players from one team on the court.")

answer5 = input("Which position usually brings the ball up the court?\n1. Center\n2. Point guard\n3. Power forward\n")
if answer5 == "2":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect. The answer is point guard.")

print("Your final score is", score, "out of 5.")

if score == 5:
    print("Perfect score! You really know basketball.")
elif score >= 3:
    print("Good job! You know a lot about basketball.")
elif score >= 1:
    print("You know some basketball.")
else:
    print("You might need to learn more about basketball.")