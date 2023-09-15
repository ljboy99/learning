import random

carddeck = ['A', '2', '3', '4', '5', '6', '7',
            '8', '9', '10', 'J', 'Q', 'K']

fulldeck = carddeck*4
playerhand = []

def drawcard():
    global carddeck, fulldeck, playerhand
    draw = random.choice(fulldeck)
    playerhand.append(draw)
    fulldeck.pop(fulldeck.index(draw))
    print(len(fulldeck))
    print(playerhand)
    drawprompt()
    return playerhand, fulldeck

askfordraw = True

def drawprompt():
    global askfordraw
    while askfordraw:
        askfordraw = input("Do you want to draw a card? ")
        if askfordraw.lower() == "y" or "yes":
            drawcard()
            askfordraw = True
            return askfordraw
        else:
            askfordraw = False
            return askfordraw


drawprompt()
