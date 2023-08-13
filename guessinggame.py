import random
answer = round(random.random()*100)
guessattempts = 0
def guessinggame():
    global guessattempts
    guessattempts += 1
    playerguess = input("Guess a number between 1 and 100. ")
    playerguess = int(playerguess)
    if playerguess == answer:
        print("Good job! it took you", guessattempts, "guesses!")
    elif playerguess > answer:
        print("It's less than that!")
        guessinggame()
    elif playerguess < answer:
        print("It's more than that!")
        guessinggame()
    else:
        print("That's not a number!")
        guessinggame()

guessinggame()