puzzle = input("Please provide an encrypted message\n")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
translation = ''
attempt = 0

def shiftone():
    global translation, alphabet, puzzle, attempt
    translation = ''
    attempt += 1
    for i in puzzle.upper():
        if i not in alphabet:
            translation += i
            continue
        newi = alphabet.index(i)
        try:
            translation += alphabet[newi+1]
        except IndexError:
            translation += alphabet[newi-26+1]
    print("Decipher attempt "+str(attempt)+": "+translation)
    puzzle = translation
    return puzzle

for f in range(25):
    shiftone()
