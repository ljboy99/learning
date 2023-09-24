inventory = {

}
i = open("inventory_list.txt", 'a')
SKU = ""
def additem():
    global SKU, inventory
    SKU = input("""Please scan product
If done, type EXPORT
    """)
    QTY = 1
    while SKU != 'EXPORT':
        if SKU not in inventory:
            inventory[SKU] = QTY
        elif SKU in inventory:
            inventory[SKU] += QTY
        additem()
    return inventory

additem()
inventory = str(inventory)
inventory = inventory.replace(', ', '\n')
inventory = inventory.replace('{', '')
inventory = inventory.replace('}', '')
i.write(inventory)
i.close()
