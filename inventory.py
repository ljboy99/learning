inventory = {

}
item = input("What item are we counting? ")
i = open(item+"_list.txt", 'a')
SKU = ""


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
    addnote = input("Would you like to add any notes? (Y/N)\n>>>")
    while addnote.capitalize() == "Y":
        i.write("NOTES\n")
        note = input("Please type your notes")
        i.write(note+"\n")
        addnote = input("Would you like to add any other notes?\n")
        i.write("------------------\n")


additem()
addnotes()
inventory = str(inventory)
inventory = inventory.replace(', ', '\n')
inventory = inventory.replace('{', '')
inventory = inventory.replace('}', '')
i.write(inventory)

i.close()
