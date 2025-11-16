def isPalindrome(s):
    # Deze functie start de recursieve controle.
    # Ze geeft de string 's' door, samen met de begin- en eindindex.
    return isPalindromeHelper(s, 0, len(s) - 1)


def isPalindromeHelper(s, low, high):
    # Base case 1: als de indexes elkaar kruisen of gelijk zijn,
    # betekent dit dat we het midden van het woord bereikt hebben.
    # Er is dan nergens een mismatch gevonden → het is een palindrome.
    if high <= low:
        return True

    # Base case 2: de karakters op low en high zijn verschillend,
    # dus kan het geen palindrome zijn.
    elif s[low] != s[high]:
        return False

    else:
        # Recursieve stap:
        # Vergelijk de volgende binnenste karakters door
        # low 1 omhoog te doen en high 1 omlaag.
        return isPalindromeHelper(s, low + 1, high - 1)


def main():
    # Testen van de functie met verschillende strings
    print("Is moon a palindrome?", isPalindrome("moon"))  # False → m != n
    print("Is noon a palindrome?", isPalindrome("noon"))  # True → n == n, o == o
    print("Is a a palindrome?", isPalindrome("a"))        # True → 1 letter = altijd palindrome
    print("Is aba a palindrome?", isPalindrome("aba"))    # True
    print("Is ab a palindrome?", isPalindrome("ab"))      # False → a != b


main()  # Call the main function.
