print('=== Army Board Study Bot ===\n')


score = 0


questions = {
    "What does NCO stand for?": "noncommissioned officer",
    "What regulation covers Army wear and appearance?": "ar 670-1",
    "How many Army Values are there?": "7",
    "What does PT stand for?": "physical training",
    "What rank is E-4?": "specialist",
    "What does AIT stand for?": "advanced individual training",
    "What does PCS stand for?": "permanent change of station",
    "What does CONUS stand for?": "continental united states",
    "What does OCONUS stand for": "outside continental united states",
    "What does MRE stand for?": "meal ready to eat", 
    "What Army regulation covers Army Leadership?": "adp 6-22",
    "How many Army Values begin with the letter L?" : "1",
    "What does ASAP stand for?": "army substance abuse program",
    "What rank is E-5?": "sergeant",
    "What rank is E-6?": "staff sergeant",
    "What rank is O-1?": "second lieutenant",
    "What does UCMJ stand for?": "uniform code of military justice",
    "What is the Army motto?": "this we'll defend",
    "What does POV stand for?": "privatley owned vehicle",
    "What does MOS stand for?": "military occupational specialty"
    }

for question, correct_answer in questions.items():


    answer = input(question+" ")
    answer = answer.strip().lower()

    if answer== correct_answer:
        print("Correcto!\n")
        score +=1
       
    else:
        print("Incorrect.")
        print("Correct Answer:", correct_answer)
        print()


print("======================")
print("Final Score:", score, "/20")

if score >= 18:
    print("🏆 BOARD READY")
elif score >= 15:
    print("✅ Almost Board Ready")
elif score >= 10:
    print ("📚 Keep Studying")
else:
    print("🚨Hit the Books, Specialist")
