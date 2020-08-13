from collections import Counter
stuff = {'coin':0,'torch':2,'helmet':1,'magic egge':1}


def DisplayInventory(inventory):
    print('Inventory: ')
    for k,v in inventory.items(): print(k, v)

    return ''


loot = {'dragon head': 0,'coin':45,'phone':1}

c  = Counter(loot)


def add(inv:dict,added):
    for l in added:

        end = ' '
        if l.lower() in inv.keys():

            inv[l] = inv[l] + c[l]


        else:

            inv[l] = c[l]


    return inv

print(DisplayInventory(stuff))
add(stuff,loot)
print(DisplayInventory(stuff))
