import urllib.request
# Importeert de urllib.request module, die functies bevat om data via HTTP/HTTPS
# van internet-URL's op te halen.
# Zonder deze import kun je geen URL openen in Python.


def main():
    url = input("Enter an URL for a file: ").strip()
    # Vraagt de gebruiker om een URL.
    # .strip() verwijdert overtollige spaties links en rechts.
    # Voorbeeld: "  https://example.com/file.txt   " → "https://example.com/file.txt"


    inputFile = urllib.request.urlopen(url)
    # urlopen(url) maakt verbinding met de opgegeven URL via HTTP(S).
    # Het resultaat is een bestand-achtig object.
    # Je kunt er .read(), .readline(), .close(), … op uitvoeren.
    #
    # De inhoud die opgehaald wordt, zijn BYTES, niet meteen tekst!


    s = inputFile.read().decode()
    # .read() leest ALLE data van de URL in één keer in.
    # Dit levert een BYTES-object, zoals: b"Hello world\n123"
    #
    # .decode() zet de bytes om naar een STRING.
    # Standaard gebruikt decode() UTF-8, wat voor bijna alle webpagina’s werkt.
    #
    # Resultaat: variabele s is nu een gewone Python-string.


    counts = countLetters(s.lower())
    # Zet de hele tekst naar kleine letters (A→a, É→


