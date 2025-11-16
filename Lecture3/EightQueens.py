from tkinter import *  # Tkinter voor GUI

SIZE = 8  # Grootte van het schaakbord (8×8)

class EightQueens:
    def __init__(self):
        self.queens = SIZE * [-1]     # Lijst met kolomposities van elke rij; -1 = geen queen geplaatst
        self.search(0)                # Start backtracking vanaf rij 0

        # ---------------- GUI ----------------
        window = Tk()                 # Maak hoofdvenster
        window.title("Eight Queens")  # Titel

        image = PhotoImage(file="image/queen.gif")  # Laad een queen-afbeelding

        # Bouw het schaakbord
        for i in range(SIZE):             # Voor elke rij
            for j in range(SIZE):         # Voor elke kolom
                if self.queens[i] == j:   # Als er een queen staat op (i, j)
                    Label(window, image=image).grid(row=i, column=j)
                else:                     # Anders teken een rood vakje
                    Label(window, width=5, height=2, bg="red").grid(
                        row=i, column=j)

        window.mainloop()  # Start de GUI-event-loop

    # ---------------- BACKTRACKING ----------------
    def search(self, row):
        if row == SIZE:     # Als we voorbij rij 7 zijn → alle queens geplaatst
            return True     # Oplossing gevonden

        for column in range(SIZE):            # Probeer alle kolommen in deze rij
            self.queens[row] = column         # Plaats queen voorlopig op (row, column)

            # Check of de positie geldig is én zoek verder op volgende rij
            if self.isValid(row, column) and self.search(row + 1):
                return True                   # Geldige oplossing gevonden → stop terugkeren

        # Geen geldige kolom gevonden in deze rij → backtrack
        return False

    # ---------------- VALIDATIE ----------------
    def isValid(self, row, column):
        # Controleer alle eerder geplaatste queens (bovenliggende rijen)
        for i in range(1, row + 1):

            # Conflicten:
            # 1. Zelfde kolom
            if self.queens[row - i] == column:
                return False
