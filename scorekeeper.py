print("Welcome to scorekeeper")
playercount = input("How many players are there? ")
playercount = int(playercount)
playerscores = {}

for i in range(playercount):
    print("Name player "+str(i+1))
    playername = input()
    playerscores[playername] = 0

print("Let's update scores!")
anotherround = True
while anotherround:
    for i in playerscores:
        score = input("How many points did "+i+" score?\n")
        playerscores[i] += int(score)
    anotherround = input("Play another round? (Y/N)")
    print("Here is the current score:")
    print(playerscores)
    if anotherround[0].upper() == "Y":
        continue
    else:
        break

print("Here is the final score")
print(playerscores)
