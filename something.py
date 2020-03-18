from collections import Counter
stuff = {'coin':42,'torch':2,'helmet':1,'magic egge':1}


def DisplayInventory(inventory):
    print('Inventory: ')
    for k,v in inventory.items(): print(k, v)

    return ''


loot = ['coin','dragon','coin','phone']

c  = Counter(loot)


def add(inv,added):
    for l in added:
        l.capitalize()

        end = ' '
        if l.lower() in inv.keys():

            inv[l] = inv[l] + c[l]

        else:

            inv[l] = c[l]

    return inv


print(add(stuff,loot))
