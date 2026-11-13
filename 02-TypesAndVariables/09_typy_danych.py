# -*- coding: utf-8 -*-
# Samodzielny przykład nr 09 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 9. TYPY DANYCH
# ---------------------------------------------------------------------------
def przyklad_09_typy_danych():
    """int (całkowite), float (dziesiętne), str (tekst), bool (logiczne)."""
    # type(wartosc) sprawdza typ wskazanej wartości.
    print(type(50))       # int: liczba całkowita, np. 50.
    print(type(149.17))   # float: liczba zmiennoprzecinkowa, np. 149.17.
    print(type('Krakow University of Economics'))  # str: napis, czyli tekst.
    print(type(2 > 5))    # bool: wynik porównania, czyli True albo False.

    # Typy wpływają na to, co Python zrobi z danymi w dalszej części kodu.


if __name__ == '__main__':
    przyklad_09_typy_danych()  # Uruchom tylko to jedno zadanie.
