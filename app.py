print("Army Board Study Bot")
print("--------------------")

score = 0

# Question 1 
answer = input("1. What does NCO stand for? ")
answer = answer.strip().lower()

if answer == "noncommissioned officer":
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect. NCO stands for Noncommissioned Officer.\n")

# Question 2
answer = input("2. what regulation covers Army uniforms and appearance?")
answer = answer.strip().lower()

if answer == "ar 670-1":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The answer is AR 670-1.\n")

# Question 3
answer = input("3. How many Army values are there?")
answer = answer.strip()

if answer == "7":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. There are 7 Army values.\n")

# Results
print("==================")
print("Final Score:", score, "/3")

if score == 3:
    print("Outstanding! Ready for the board.")
elif score == 2:
    print("Good Job. Study a little more.")
elif score == 1:
    print("Keep Studying.")
else:
    print("Hit the books, Specialist.")
