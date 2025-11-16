class Heap:
    def __init__(self):
        self.__lst = []                   # Interne lijst voor de heap (complete binaire boom)

    # -----------------------------------------
    # Add a new item into the heap
    # -----------------------------------------
    def add(self, e):
        self.__lst.append(e)              # Voeg element onderaan (laatste plek) toe
        currentIndex = len(self.__lst) - 1  # Index van nieuw element

        # "Percolate up" → naar boven schuiven zolang het groter is dan de ouder
        while currentIndex > 0:
            parentIndex = (currentIndex - 1) // 2  # Index van ouder in heap-structuur

            # Als huidig element groter is dan zijn ouder → swap
            if self.__lst[currentIndex] > self.__lst[parentIndex]:
                self.__lst[currentIndex], self.__lst[parentIndex] = \
                    self.__lst[parentIndex], self.__lst[currentIndex]
            else:
                break                       # Heap-eigenschap is hersteld

            currentIndex = parentIndex      # Ga verder omhoog


    # -----------------------------------------
    # Remove the max element (root) from the heap
    # -----------------------------------------
    def remove(self):
        if len(self.__lst) == 0:
            return None                     # Lege heap → niets te verwijderen

        removedItem = self.__lst[0]         # Grootste element (root)
        self.__lst[0] = self.__lst[-1]      # Verplaats laatste element naar de top
        self.__lst.pop()                    # Verwijder laatste element

        # "Percolate down" → grote elementen bovenaan duwen
        currentIndex = 0
        while currentIndex < len(self.__lst):

            leftChildIndex = 2 * currentIndex + 1
            rightChildIndex = 2 * currentIndex + 2

            # Als er geen linker kind is → we zitten onderaan de boom
            if leftChildIndex >= len(self.__lst):
                break

            # Kies de grootste van de twee kinderen
            maxIndex = leftChildIndex
            if rightChildIndex < len(self.__lst):
                if self.__lst[rightChildIndex] > self.__lst[maxIndex]:
                    maxIndex = rightChildIndex

            # Als ouder kleiner is dan de grootste van de kinderen → swap
            if self.__lst[currentIndex] < self.__lst[maxIndex]:
                self.__lst[currentIndex], self.__lst[maxIndex] = \
                    self.__lst[maxIndex], self.__lst[currentIndex]
                currentIndex = maxIndex     # Ga verder naar beneden
            else:
                break                       # Heap-eigenschap is hersteld

        return removedItem                  # Return het verwijderde max-element


    # ----------------- EXTRA METHODS ---------------------
    def getSize(self):
        return len(self.__lst)

    def isEmpty(self):
        return self.getSize() == 0

    def peek(self):
        return self.__lst[0]                # Grootste element (root)

    def getLst(self):
        return self.__lst                   # Volledige interne lijst
