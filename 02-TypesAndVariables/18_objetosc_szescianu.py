# -*- coding: utf-8 -*-
# Samodzielny przykład nr 18 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 18. TYPE CONVERSION — KONWERSJA TEKSTU NA LICZBĘ
# ---------------------------------------------------------------------------
def przyklad_18_objetosc_szescianu():
    """Wczytujemy długość boku i obliczamy objętość a ** 3."""
    # input() zawsze daje str; przechowujemy go początkowo w zmiennej tekstowej.
    cube_side_string = input('Enter cube side: ')

    # int(tekst) zamienia poprawnie zapisane cyfry na liczbę całkowitą.
    cube_side = int(cube_side_string)

    # ** 3 oznacza trzecią potęgę, czyli a * a * a (objętość sześcianu).
    volume = cube_side ** 3
    print(volume)  # Wyświetlamy otrzymaną objętość.

    # Przydatne konwersje innych typów (przykłady dodatkowe):
    a = int('10')     # Tekst '10' zamieniamy na liczbę całkowitą 10.
    b = float('10.5') # Tekst '10.5' zamieniamy na float 10.5.
    c = str(10)       # Liczbę 10 zamieniamy na tekst '10'.
    print(a, b, c)    # Pokazujemy efekty trzech konwersji.

    # int('10.5') spowodowałoby błąd: tekst zawiera część dziesiętną.
    # W Pythonie do zapisu wartości dziesiętnych używa się kropki, np. 5.5.


if __name__ == '__main__':
    przyklad_18_objetosc_szescianu()  # Uruchom tylko to jedno zadanie.
