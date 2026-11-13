# -*- coding: utf-8 -*-
# Samodzielny przykład nr 10 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 10. WPŁYW TYPU DANYCH NA ZACHOWANIE OPERATORÓW
# ---------------------------------------------------------------------------
def przyklad_10_operator_a_typ():
    """Porównujemy działanie + i * na różnych rodzajach wartości."""
    print(2 + 3)       # Liczby int są dodawane matematycznie.
    print('2' + '3')   # Napisy str są łączone, a nie dodawane matematycznie.
    print(4 * 7)       # Mnożenie dwóch liczb całkowitych daje liczbę całkowitą.
    print(4.0 * 7)     # Użycie float sprawia, że wynik ma typ float.

    # '5' jest tekstem, a 5 jest liczbą — NIE są tym samym typem danych.


if __name__ == '__main__':
    przyklad_10_operator_a_typ()  # Uruchom tylko to jedno zadanie.
