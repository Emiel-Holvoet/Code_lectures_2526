def main():
    filename = input("Enter a filename: ").strip()
    # Vraagt de gebruiker om een bestandsnaam.
    # .strip() verwijdert spaties/nieuwe regels aan begin en einde.
    # Voorbeeld: gebruiker typt "  text.txt  " → wordt "text.txt"

    inputFile = open(filename, "r")   # Open het bestand in read-modus ("r").
                                      # inputFile wordt een file-object dat je kunt doorlopen.

    counts = 26 * [0]                 # Maak een lijst van 26 nullen → één plek voor elke letter.
                                      # index 0 = 'a'
                                      # index 1 = 'b'
                                      # ...
                                      # index 25 = 'z'

    for line in inputFile:
        # Deze for-loop leest het bestand **regel per regel**.
        # 'line' bevat telkens 1 volledige tekstregel als string.

        countLetters(line.lower(), counts)
        # .lower() zet de hele regel om naar kleine letters (A → a),
        # zodat we geen onderscheid hoeven te maken tussen hoofdletters en kleine letters.
        #
        # countLetters telt het aantal letters in deze regel en
        # verhoogt de juiste teller in counts[].


    # ------- RESULTATEN WEERGEVEN -------
    for i in range(len(counts)):
        # loop over indices 0 t.e.m. 25

        if counts[i] != 0:
            # Alleen letters tonen die werkelijk voorkomen.

            print(
                chr(ord('a') + i)      # Zet index 0 → 'a', index 1 → 'b', ...
                + " appears "
                + str(counts[i])        # Hoe vaak?
                + (" time" if counts[i] == 1 else " times")
                # Klein grammatica-detail:
                # 1 time  maar  2 times
            )

    inputFile.close()                  # Bestand sluiten (goede gewoonte)

  
# -------- HULPFUNCTIE: TEL LETTERS ---------

def countLetters(line, counts):
    for ch in line:
        # Loop door elk karakter in de regel

        if ch.isalpha():               # Controleer of het karakter een LETTER is (a-z, A-Z)
            counts[ord(ch) - ord('a')] += 1
            # UITLEG VAN DIT BELANGRIJKE TRUUKJE:
            #
            # ord(ch)  → geeft ASCII/Unicode nummer van de letter
            # ord('a') → ascii van 'a'
            #
            # ord(ch) - ord('a') geeft:
            #   'a' → 0
            #   'b' → 1
            #   'c' → 2
            #   ...
            #   'z' → 25
            #
            # Precies de index die we nodig hebben!
