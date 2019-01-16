import os 
import random

    

def main():
    print "The number game\n =========================="
    print "I am guessing a number between 0 and 200.\n Can you guess it "
    userName = raw_input("What's your name?: ")
    randomNumber = random.randrange(200)
    userGuess = ""

    messagesFile = open("motivation.txt", "r")
    motivationList = messagesFile.read().splitlines()
    messagesFile.close()
    userMotivations = map(lambda motivation: "**" + motivation + ", " + userName + "! **", motivationList)

    while userGuess != randomNumber: 
        # get the users guess
        # compare guess against randomNumber 
        userGuess = int(raw_input("Your guess:"))
        if userGuess < randomNumber:
            print random.choice(userMotivations)
            print  'Your guess was too low'
        elif userGuess > randomNumber:
            print random.choice(userMotivations)
            print "Your guess was too high"
    print "****You did it*****"

    raw_input()

main()
