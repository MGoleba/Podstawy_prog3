# -*- coding: utf-8 -*-
# Samodzielny przykład nr 07 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 07. EVEN OR ODD — LICZBA PARZYSTA CZY NIEPARZYSTA?
# ===========================================================================
def przyklad_07_parzystosc():
    """Operator modulo (%) pomaga odróżnić liczby parzyste od nieparzystych."""
    number = int(input('Enter number: '))  # Pobieramy liczbę całkowitą.

    # number % 2 to reszta z dzielenia liczby przez 2.
    # == 0 sprawdza, czy pozostała reszta równa zero.
    # Dla 8 % 2 otrzymujemy 0; dla 7 % 2 otrzymujemy 1.
    if number % 2 == 0:               # Warunek True oznacza liczbę parzystą.
        print(f'{number} is even')     # f-string wstawia liczbę w miejsce {number}.
    else:                              # Reszta nie jest 0, więc liczba jest nieparzysta.
        print(f'{number} is odd')      # Wyświetlamy komunikat o nieparzystości.


if __name__ == '__main__':
    przyklad_07_parzystosc()  # Uruchom tylko to jedno zadanie.
