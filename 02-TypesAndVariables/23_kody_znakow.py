# -*- coding: utf-8 -*-
# Samodzielny przykład nr 23 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 23. CHARACTERS AND CODES — ZNAKI I KODY UNICODE
# ---------------------------------------------------------------------------
def przyklad_23_kody_znakow():
    """Zamiana znaku na kod i obliczenie liczby liter między A a D."""
    print(ord('A'))  # ord(znak) zwraca kod Unicode podanego znaku.
    print(ord('B'))  # Dla dużej litery B kod wynosi 66.
    print(chr(67))   # chr(kod) zwraca znak odpowiadający liczbie 67.

    first = 'A'  # Pierwsza litera badanego zakresu.
    last = 'D'   # Ostatnia litera badanego zakresu.

    # ord(last) zamienia D na 68; ord(first) zamienia A na 65.
    # Odejmujemy 1, bo nie liczymy żadnej z liter krańcowych.
    # Pomiędzy A a D są tylko B i C, czyli dokładnie dwa znaki.
    letters_between = ord(last) - ord(first) - 1
    print(letters_between)  # Wyświetlamy liczbę liter pomiędzy A i D.

    # Liczenie różnic kodów działa w ten sposób dla kolejnych liter A–Z.


if __name__ == '__main__':
    przyklad_23_kody_znakow()  # Uruchom tylko to jedno zadanie.
