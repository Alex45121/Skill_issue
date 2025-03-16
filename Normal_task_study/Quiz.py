print("Wel;come to my QUIZ")

score = 0
playing = input("Do you want to play?\n ")


if playing.lower() != "yes":
    quit()

print("okay G les go")

answer = input("What does CPU stand for?\n ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("incorrect")
    score -= 1

answer = input("When was bulgaria founder?\n ")
if answer == "681":
    print("Correct")
    score += 1
else:
    print("incorrect")
    score -= 1



answer = input("what does ram stand for?\n ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("incorrect")
    score -= 1

if score >= 2:
    print(f"congrats G you not stoopid, you score was {score}")
else:
    print(f"G you dumb af, you score was {score}")
