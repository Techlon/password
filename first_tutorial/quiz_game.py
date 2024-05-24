print ("Hello World")

playing = input ("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay Let's Play")
score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("INcorrect")

answer = input("What does RAM stand for? ")

if answer.upper() == "RANDOM ACCESS MEMORY":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print ("You got " + str(score) + " questions right.")
print ("You got " + str((score/3)*100) + " % questions right.")

