import os

def main():
    # Vraag de gebruiker om een pad naar een directory of bestand
    path = input("Enter a directory or a file: ").strip()

    # Toon de totale grootte in bytes
    try:
        print(getSize(path), "bytes")
    except:
        print("Directory or file does not exist")


def getSize(path):
    size = 0                     # Totaal aantal bytes dat we gaan optellen

    # Check of het GEEN bestand is → dus een directory
    if not os.path.isfile(path):
        lst = os.listdir(path)   # Haal alle bestanden/submappen binnen de directory op

        # Loop door elke naam in de directory
        for subdirectory in lst:
            # Roep getSize RECURSIEF aan op elk subpad
            # path + "\\" + subdirectory vormt het volledige pad
            size += getSize(path + "\\" + subdirectory)

    else:
        # Base case: het pad is een bestand
        # Neem de grootte van dit bestand en tel op
        size += os.path.getsize(path)

    return size


main()  # Start het programma
