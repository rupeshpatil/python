def binarySearch(item, itemlist):
    first = 0
    last = len(itemlist) -1
    found = False
    while first <= last and not found:
        middle = (first + last) //2
        if itemlist[middle] == item:
            found = True
        elif itemlist[middle] < item:
            first = middle + 1
        else:
            last = middle - 1
    return found

binarySearch(12, [34,45,12,34,56,67,78].sort())