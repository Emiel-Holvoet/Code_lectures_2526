def bubbleSort(lst):
    needNextPass = True           # Deze vlag bepaalt of we nog een extra ronde moeten doen
    
    k = 1                         # k = hoeveel elementen al achteraan gesorteerd zijn
    while k < len(lst) and needNextPass:
        # Als in de vorige ronde geen swaps gebeurden, is de lijst al gesorteerd
        needNextPass = False

        # Loop door alle elementen tot len(lst) - k
        # De laatste k elementen staan al op hun juiste plek
        for i in range(len(lst) - k):

            # Vergelijk elk element met zijn buur
            if lst[i] > lst[i + 1]:
                # Verwissel de twee elementen
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp

                needNextPass = True  # Er was een swap → lijst was nog niet gesorteerd

        k += 1                      # Na elke pass komt het grootste element achteraan op z’n plek


def main():
    lst = [2, 3, 2, 5, 6, 1]()

