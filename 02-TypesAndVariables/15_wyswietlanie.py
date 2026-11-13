# -*- coding: utf-8 -*-
# Samodzielny przykład nr 15 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 15. PROGRAM OUTPUT — WYŚWIETLANIE WYNIKU
# ---------------------------------------------------------------------------
def przyklad_15_wyswietlanie():
    """Suma dwóch liczb oraz opis wyniku w funkcji print()."""
    number1 = 71  # Pierwsza liczba, którą chcemy dodać.
    number2 = 14  # Druga liczba, którą chcemy dodać.
    result = number1 + number2  # + dodaje obie wartości; zapisujemy sumę.

    # Pierwszy argument print() to tekst, drugi to wartość zmiennej result.
    # Print domyślnie oddziela kolejne argumenty spacją.
    print('The result of summation:', result)


if __name__ == '__main__':
    przyklad_15_wyswietlanie()  # Uruchom tylko to jedno zadanie.
