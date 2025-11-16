class LinkedList:
    def __init__(self):
        self.__head = None      # Verwijzing naar het eerste knooppunt (Node) in de lijst. 
                                # None betekent: lijst is leeg.
        self.__tail = None      # Verwijzing naar het laatste knooppunt in de lijst.
                                # Ook None als de lijst leeg is.
        self.__size = 0         # Houdt bij hoeveel elementen er in de lijst zitten.


    # ---------- BASISMETHODEN ----------
    
    # Return the head element in the list 
    def getFirst(self):
        if self.__size == 0:            # Controle: lijst is leeg → geen head
            return None
        else:
            return self.__head.element  # Anders: geef het element van de eerste Node terug
    
    # Return the last element in the list 
    def getLast(self):
        if self.__size == 0:            # Lijst is leeg → geen tail
            return None
        else:
            return self.__tail.element  # Anders: element in de laatste Node teruggeven


    # ---------- TOEVOEGEN ----------

    # Add an element to the beginning of the list 
    def addFirst(self, e):
        newNode = Node(e)               # Maak een nieuwe Node met element e
        newNode.next = self.__head      # De nieuwe Node wijst naar de huidige head
        self.__head = newNode           # De head verwijst nu naar de nieuwe Node
        self.__size += 1                # Verhoog de grootte van de lijst

        if self.__tail == None:         # Als de lijst leeg wás, is de nieuwe Node zowel head als tail
            self.__tail = self.__head

    # Add an element to the end of the list 
    def addLast(self, e):
        newNode = Node(e)               # Maak een nieuwe Node met e
    
        if self.__tail == None:         # Lijst is leeg
            self.__head = self.__tail = newNode  # Head en tail worden dezelfde Node
        else:
            self.__tail.next = newNode  # Laatste Node wijst naar de nieuwe Node
            self.__tail = self.__tail.next  # Tail verschuift naar de nieuwe laatste Node
    
        self.__size += 1                # Verhoog de lijstgrootte

    # Same as addLast 
    def add(self, e):                    # Simpele alias
        self.addLast(e)


    # ---------- INVOEGEN ----------

    # Insert a new element at the specified index
    def insert(self, index, e):
        if index == 0:                   # Vooraan toevoegen
            self.addFirst(e)
        elif index >= self.__size:       # Achteraan toevoegen
            self.addLast(e)
        else:                            # In het midden invoegen
            current = self.__head        # Start bij de head
            for i in range(1, index):    # Loop totdat we bij de Node vóór de insert-plek zijn
                current = current.next

            temp = current.next          # Tijdelijke verwijzing naar de rest van de lijst
            current.next = Node(e)       # Nieuwe Node invoegen
            (current.next).next = temp   # Nieuwe Node verbinden met de rest
            self.__size += 1             # Grootte +1


    # ---------- VERWIJDEREN ----------

    # Remove the head node
    def removeFirst(self):
        if self.__size == 0:                 # Kan niets verwijderen als lijst leeg is
            return None
        else:
            temp = self.__head               # Bewaar eerste Node
            self.__head = self.__head.next   # Verplaats head één Node verder
            self.__size -= 1                 # Size --

            if self.__head == None:          # Als lijst nu leeg is
                self.__tail = None           # Tail moet ook None worden

            return temp.element              # Return het verwijderde element

    # Remove the last node
    def removeLast(self):
        if self.__size == 0:                 # Lege lijst
            return None
        elif self.__size == 1:               # Lijst met 1 element
            temp = self.__head               # Bewaar het enige element
            self.__head = self.__tail = None # Maak lijst leeg
            self.__size = 0
            return temp.element
        else:
            current = self.__head            # Begin bij de head
        
            for i in range(self.__size - 2): # Loop naar de Node vóór de tail
                current = current.next
        
            temp = self.__tail               # Bewaar de tail Node
            self.__tail = current            # De nieuwe tail is de Node ervoor
            self.__tail.next = None          # Tail mag nergens naar wijzen
            self.__size -= 1
            return temp.element              # Return verwijderde element


    # Remove element op index
    def removeAt(self, index):
        if index < 0 or index >= self.__size:   # Ongeldige index
            return None
        elif index == 0:
            return self.removeFirst()           # Verwijder eerste Node
        elif index == self.__size - 1:
            return self.removeLast()            # Verwijder laatste Node
        else:
            previous = self.__head              # Begin bij head
    
            for i in range(1, index):           # Loop tot Node vóór te verwijderen Node
                previous = previous.next
        
            current = previous.next             # Node die verwijderd moet worden
            previous.next = current.next        # Sla de verwijderde Node over
            self.__size -= 1                    # Grootte --
            return current.element              # Return het verwijderde element


    # ---------- INFORMATIE ----------
    
    def isEmpty(self):
        return self.__size == 0                 # True als geen elementen
    
    def getSize(self):
        return self.__size                      # Grootte teruggeven


    # ---------- STRINGWEERGAVE ----------

    def __str__(self):
        result = "["                             # Start string

        current = self.__head                    # Start bij head
        for i in range(self.__size):             # Voor elk element
            result += str(current.element)       # Voeg element toe
            current = current.next               # Ga naar volgende Node

            if current != None:
                result += ", "                   # Komma tussen elementen
            else:
                result += "]"                    # Sluit af met ]

        return result                            # Geef string terug


    # ---------- EXTRA METHODEN (NIET GEÏMPLEMENTEERD) ----------

    def clear(self):
        self.__head = self.__tail = None         # Verwijder alle links
                                                  # __size zou ook op 0 moeten gezet worden (bug)

    def contains(self, e):
        print("Implementation left as an exercise")
        return True

    def remove(self, e):
        print("Implementation left as an exercise")
        return True

    def get(self, index):
        print("Implementation left as an exercise")
        return None

    def indexOf(self, e):
        print("Implementation left as an exercise")
        return 0

    def lastIndexOf(self, e):
        print("Implementation left as an exercise")
        return 0

    def set(self, index, e):
        print("Implementation left as an exercise")
        return None
    
    # Maakt indexering mogelijk: lijst[3]
    def __getitem__(self, index):
        return self.get(index)

    # Iterator zodat je 'for x in list:' kunt gebruiken
    def __iter__(self):
        return LinkedListIterator(self.__head)
    

# ---------- NODE KLASSE ----------
class Node:
    def __init__(self, e):
        self.element = e     # Het opgeslagen element
        self.next = None     # Verwijzing naar de volgende Node (of None)


# ---------- ITERATOR ----------
class LinkedListIterator: 
    def __init__(self, head):
        self.current = head    # Beginnen bij de head
        
    def __next__(self):
        if self.current == None:       # Geen elementen meer → stop iterator
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next  # Ga naar de volgende Node
            return element


        
