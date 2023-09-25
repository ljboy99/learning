import os

if os.path.isdir("OUTPUT/") == False: ### Verify that the output folder exists
    os.mkdir("OUTPUT/") ### If OUTPUT directory doesn't exist, make it.

inventory = {

}

def defineCurrentItem():
    print("Current files that exist are: \n"+str(os.listdir("OUTPUT/")))
    item = input("""What item are we counting? """)
    global i
    i = open("OUTPUT/"+item+"_list.txt", 'a')
    return i

SKU = ""

#def viewlist(): ### Figuring this out, not using it for now
    #view = input("Would you like to view your inventory? (Y/N)\n")
    #if view[0].upper == "Y":
        #print(os.path.listdir("OUTPUT/"))

def additem():
    global SKU, inventory
    print("""Please scan product
If done, type EXPORT""")
    SKU = input()
    QTY = 1
    while SKU != 'EXPORT':
        if SKU not in inventory:
            inventory[SKU] = QTY
        elif SKU in inventory:
            inventory[SKU] += QTY
        additem()
    return inventory

def addnotes():
    global i
    addnote = input("Would you like to add any notes? (Y/N)\n>>>")
    while addnote.capitalize() == "Y":
        i.write("NOTES\n")
        note = input("Please type your notes")
        i.write(note+"\n")
        addnote = input("Would you like to add any other notes?\n")
        i.write("------------------\n")

def writetoinventory():
    global i
    global inventory
    inventory = str(inventory)
    inventory = inventory.replace(', ', '\n')
    inventory = inventory.replace('{', '')
    inventory = inventory.replace('}', '')
    i.write(inventory)

defineCurrentItem()
#viewlist()
additem()
addnotes()
writetoinventory()

i.close()
