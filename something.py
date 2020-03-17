from collections import Counter
stuff = {'coin':42,'torch':2,'helmet':1,'magic egge':1}
def DisplayInventory(inventory):
    print('Inventory: ')
    for k,v in stuff.items(): print(k, v)

    return ''


loot = ['coin','dragons head','coin','d','coin','a','coin']
c  = Counter(loot)
def add(inv,added):
    for l in added:
        if l in inv.keys():
            inv[l] = inv[l] + c[l]
            break
        else:
            pass
            #ВОТ ТУТ НАДО ДОБАВИТЬ ДРУГИЕ ЭЛЕМЕНТЫ КОТОРЫХ НЕТ



    return inv




print(add(stuff,loot))
