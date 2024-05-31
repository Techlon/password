name = input ("What is your name: ")
print ("Welcome", name, "to the adventure of a wanderer")

q1 = input("You are at the end of a dirt road and need to choose where to go. Left or Right: ").lower()

if q1 == "left":
    print ("You have two options - Down the Staircase or Go up the elevator - STAIRCASE or ELEVATOR: ")
    q2 = input ("STAIRCASE or ELEVATOR: ").lower()
    if q2 == "staircase":
        print ("You won")
    elif q2 == "elevator":
        print ("Elevator closes on you and you lose")

elif q1 == "right":
    print ("Well done, you have come a long way. Next Step ahaead")
    print ("Either choose to use the Ferry or go by Speed Boat: FERRY or BOAT")
    q3 = input("Choose either Ferry or Boat: ").lower()
    if q3 == "ferry":
        print ("You have taken the slower but safer means, well done")
    if q3 == "boat":
        print ("Faster way out.")

else:
    print ("wrong answer, replay.")
    quit()