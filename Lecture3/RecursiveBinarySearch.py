def recursiveBinarySearch(lst, key):
    # Start de binaire zoekopdracht over de volledige lijst
    low = 0
    high = len(lst) - 1
    return recursiveBinarySearchHelper(lst, key, low, high)


def recursiveBinarySearchHelper(lst, key, low, high):
    # Base case 1: als low > high, is het zoekgebied leeg.
    # Dat betekent dat de key NIET in de lijst zit.
    # De waarde -low-1 is een conventionele manier om te tonen
    # waar de key zou moeten worden ingevoegd.
    if low > high:
        return -low - 1

    # Bereken de middenindex
    mid = (low + high) // 2

    # Als de key kleiner is dan het middenelement → zoek links
    if key < lst[mid]:
        return recursiveBinarySearchHelper(lst, key, low, mid - 1)

    # Als de key gelijk is aan het middenelement → gevonden!
    elif key == lst[mid]:
        return mid

    # Anders → key is groter dan middenelement → zoek rechts
    else:
        return recursiveBinarySearchHelper(lst, key, mid + 1, high)


def main():
    lst = [3, 5, 6, 8, 9, 12, 34, 36]
    print(recursiveBinarySearch(lst, 3))  # 3 zit op index 0
    print(recursiveBinarySearch(lst, 4))  # 4 zit niet in lijst → negatieve invoegindex

main()
