import random

#r = random.randrange(-5,11)
#print (r)

#p = random.randint(-3, 11)
#print (p)
top_of_range = input("Please input a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print ("Write a number greater than 0, next time")
        quit()
else:
    print ("Write a real number")
    quit()

random_number = random.randint(0, top_of_range)
print(random_number)
guesses = 0

while True:
    guesses += 1                                     #Now that we have our random number, we want the user to type in a guess for the number until they get it correct.
    user_question = input("Make a guess: ")
    if user_question.isdigit():
        user_question = int(user_question)
    else:
        print("Write a number next time")
        continue
    if user_question == random_number:
        print ("You got it!")
        break
    elif user_question > random_number:
        print("You were above the random number")
    else:
        print("You were below the number")
print ("You have gotten it in", guesses, "guesses")