print("Army Board Study Bot")
print("--------------------")

score = 0

answer = input("1. What does NCO stand for? ")
answer = answer.strip().lower()

if answer == "noncommissioned officer":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect. NCO stands for Noncommissioned Officer.")

print("Your final score is", score, "out of 1")
