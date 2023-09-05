import random
print("""The Monty Hall problem is a challenge
which questions the probability of having the
optimal outcome when you chosen one of 3 options
but change your mind after revealing one.""")

outcomes = ["WRONG", "WRONG", "CORRECT!"]
doors = {
    "DOOR 1":"",
    "DOOR 2":"",
    "DOOR 3":""
}

def assignment():
    door1 = random.choice(outcomes)
    doors["DOOR 1"] = door1
    outcomes.remove(door1)
    door2 = random.choice(outcomes)
    doors["DOOR 2"] = door2
    outcomes.remove(door2)
    door3 = random.choice(outcomes)
    doors["DOOR 3"] = door3
    outcomes.remove(door3)

assignment()

selections = input("""
You are presented with
three doors. One contains a path to freedom,
the others will lead you to a certain death. 
Which door shall you open?
>>> DOOR """)

if selections == "1":
    print("You selected door 1.")
    print("But what was behind door 3?")
    print("Door 3 was "+doors["DOOR 3"])
    if doors["DOOR 3"] == "CORRECT!":
        print("Well, we're certain you wont survive now\nGAME OVER")
    else:
        keepchoice = input("Exciting. Do you want to stick to door 1? Y/N\n>>> ")
        if keepchoice == "Y" or "y":
            print("Alright then, let's open door 1!\nDoor 1 was "+doors["DOOR 1"])
            if doors["DOOR 1"] == "CORRECT!":
                print("YOU'VE SURVIVED!")
            else:
                print("HAHA. CERTAIN DEATH. GAME OVER!")
        else:
            print("Clever, let's open door 2\nDoor 2 was "+doors["DOOR 2"])
            if doors["DOOR 2"] == "CORRECT!":
                print("YOU'VE SURVIVED!")
            else:
                print("HAHA. CERTAIN DEATH. GAME OVER!")
elif selections == "2":
    print("You selected door 2.")
    print("But what was behind door 1")
    print("Door 1 was "+doors["DOOR 1"])
    if doors["DOOR 1"] == "CORRECT!":
        print("Well, we're certain you wont survive now\nGAME OVER")
    else:
        keepchoice = input("Exciting. Do you want to stick to door 2? Y/N\n>>> ")
        if keepchoice == "Y" or "y":
            print("Alright then, let's open door 2!\nDoor 2 was "+doors["DOOR 2"])
            if doors["DOOR 2"] == "CORRECT!":
                print("YOU'VE SURVIVED!")
            else:
                print("HAHA. CERTAIN DEATH. GAME OVER!")
        else:
            print("Clever, let's open door 3\nDoor 3 was "+doors["DOOR 3"])
            if doors["DOOR 3"] == "CORRECT!":
                print("YOU'VE SURVIVED!")
            else:
                print("HAHA. CERTAIN DEATH. GAME OVER!")
elif selections == "3":
    print("You selected door 3.")
    print("But what was behind door 1")
    print(doors["DOOR 1"])
    if doors["DOOR 1"] == "CORRECT!":
        print("Well, we're certain you wont survive now\nGAME OVER")
    else:
        keepchoice = input("Exciting. Do you want to stick to door 3? Y/N\n>>> ")
        if keepchoice == "Y" or "y":
            print("Alright then, let's open door 3!\nDoor 3 was "+doors["DOOR 3"])
            if doors["DOOR 3"] == "CORRECT!":
                print("YOU'VE SURVIVED!")
            else:
                print("HAHA. CERTAIN DEATH. GAME OVER!")
        else:
            print("Clever, let's open door 2\nDoor 2 was "+doors["DOOR 2"])
            if doors["DOOR 2"] == "CORRECT!":
                print("YOU'VE SURVIVED!")
            else:
                print("HAHA. CERTAIN DEATH. GAME OVER!")