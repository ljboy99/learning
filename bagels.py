# https://inventwithpython.com/bigbookpython/project1.html

import random

guesscount = 10
win = None
answer = ''
def generate():
  global answer
  answer = str(random.randrange(100,1000))
  return answer



def guess():
  global guesscount, answer, win
  response = ""
  userguess = input(f"""I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
  You have {guesscount} guesses to get it.
""")
  if userguess[0] == answer[0] and userguess[1] == answer[1] and userguess[2] == answer[2]:
    print("You got it!")
    #win = True
    playagain()
  else: 
    while True:
      if userguess[0] in answer:
        if userguess[0] == answer[0]:
          response += "Fermi "
        else:
          response += "Pico "
      if userguess[1] in answer:
        if userguess[1] == answer[1]:
          response += "Fermi "
        else:
          response += "Pico "
      if userguess[2] in answer:
        if userguess[2] == answer[2]:
          response += "Fermi "
        else:
          response += "Pico "
      print(response)
      break
  guesscount -= 1
  return guesscount, win

def playagain():
  global guesscount, win
  play = input("Would you like to play again? (Y/N) \n")
  if play.upper() == "Y":
    guesscount = 10
    generate()
    guess()
  else:
    win = True

def game():
  global guesscount, answer
  generate()
  print(answer)
  guesscount = 10
  while guesscount > 0 and win != True:
    guess()

game()

