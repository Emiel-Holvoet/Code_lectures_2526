from Heap import Heap

class PriorityQueue:
    def __init__(self):
        self.__heap = Heap()           # Interne heap die de prioriteiten beheert

    # Voeg een element toe aan de priority queue
    def enqueue(self, e):
        self.__heap.add(e)             # In een max-heap komt het grootste element bovenaan

    # Verwijder het element met de hoogste prioriteit
    def dequeue(self):
        if self.getSize() == 0:        # Queue leeg?
            return None
        else:
            return self.__heap.remove()  # remove() haalt de root van de heap weg (max element)

    # Geef de grootte van de queue terug
    def getSize(self):
        return self.__heap.getSize()    # Aantal elementen in de heap

