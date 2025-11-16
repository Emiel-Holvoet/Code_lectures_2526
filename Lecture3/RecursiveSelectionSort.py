def sort(lst):
    # Start het sorteerproces voor de volledige lijst
    sortHelper(lst, 0, len(lst) - 1)  # Sorteer van index 0 tot laatste index


def sortHelper(lst, low, high):
    # De lijst moet enkel worden gesorteerd als low < high
    # Wanneer low == high of low > high, is er 0 of 1 element → automatisch gesorteerd
    if low < high:

        # Zoek het kleinste element in het bereik lst[low .. high]
        indexOfMin = low              # Ga ervan uit dat het eerste element het kleinst is
        min = lst[low]                # Bewaar de waarde van dit element

        # Loop door de rest van het bereik om een kleiner element te zoeken
        for i in range(low + 1, high + 1):
            if lst[i] < min:          # Als een kleiner element wordt gevonden,
                min = lst[i]          # update dan de minimumwaarde
                indexOfMin = i        # en onthoud de index ervan

        # Wissel het kleinste element met het element op positie 'low'
        lst[indexOfMin] = lst[low]    # Zet het element van 'low' op de plek van de min
        lst[low] = min                # Zet de min op de juiste positie vooraan

        # Sorteer de rest van de lijst vanaf low+1
        sortHelper(lst, low + 1, high)  # Recursieve oproep


def main():
    lst = [3, 2, 1, 5, 9, 0]  # Ongeordende lijst
    sort(lst)                # Sorteer de lijst
    print(lst)               # Toon het resultaat
