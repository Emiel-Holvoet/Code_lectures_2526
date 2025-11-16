from LinkedList import LinkedList      # Importeer jouw LinkedList–implementatie,
                                      # zodat de Queue intern een LinkedList kan gebruiken.


class Queue:
    def __init__(self):
        self.__elements = LinkedList() # Maak een lege LinkedList die zal fungeren
                                       # als de opslagstructuur voor de queue.
                                       # Queue werkt FIFO, en een linked list is daar geschikt voor.


    # ---------- ELEMENT TOEVOEGEN ----------

    # Adds an element to this queue
    def enqueue(self, e):
        self.__elements.add(e)         # Voeg element e toe aan het einde van de linked list.
                                       # add() is hetzelfde als addLast(), dus e komt achteraan in de queue.
                                       # Dit zorgt ervoor dat enqueue altijd O(1) duurt.


    # ---------- ELEMENT VERWIJDEREN ----------

    # Removes an element from this queue
    def dequeue(self):
        if self.getSize() == 0:        # Als queue leeg is → niets om te verwijderen.
            return None
        else:
            return self.__elements.removeAt(0)
                                       # Verwijder het element aan het begin van de linked list.
                                       # removeAt(0) verwijdert de head.
                                       # Dat is precies wat een queue doet: FIFO.
                                       # Ook dit duurt O(1), omdat linked list heads snel verwijderd kunnen worden.


    # ---------- GROOTTE TERUGGEVEN ----------

    # Return the size of the queue
    def getSize(self):
        return self.__elements.getSize()
                                       # Vraag de grootte op via de linked list.
                                       # LinkedList beheert zelf een __size variabele → O(1) tijd.


    # ---------- STRING WEERGAVE ----------

    # Returns a string representation of the queue
    def __str__(self):
        return self.__elements.__str__()
                                       # Gebruik de stringweergave van de LinkedList.
                                       # De queue wordt dus afgedrukt als een lijst zoals: [5, 9, 12]


    # ---------- IS LEEG? ----------

    # Return true if queue is empty 
    def isEmpty(self):
        return self.getSize() == 0      # Queue is leeg als grootte 0 is.
