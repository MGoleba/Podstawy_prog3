# -*- coding: utf-8 -*-
# Samodzielny przykład nr 06 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 06. BOOLEAN FLAG — ZMIENNA LOGICZNA Z INFORMACJĄ O ZALICZENIU
# ===========================================================================
def przyklad_06_flaga_zaliczenie():
    """Wynik porównania zapisujemy pod nazwą test_passed."""
    total_tasks = 20  # Wszystkich zadań jest 20.
    tasks_ok = int(input('Correct tasks: '))  # Użytkownik podaje liczbę poprawnych.

    # total_tasks * 0.5 oznacza połowę wszystkich zadań (w tym przypadku 10).
    # >= sprawdza, czy liczba poprawnych jest większa LUB RÓWNA połowie.
    # Wartość True/False zapisujemy w zmiennej test_passed (flaga logiczna).
    test_passed = tasks_ok >= total_tasks * 0.5  # Flaga: czy test zaliczony?

    # W if można wpisać samą zmienną logiczną; nie potrzeba „== True”.
    if test_passed:  # Gdy test_passed ma wartość True...
        print('Congratulations! You passed the test.')  # Komunikat o zaliczeniu.
    else:  # Wykonuje się, gdy test_passed ma wartość False.
        print('Unfortunately, you failed the test.')  # Komunikat o niezaliczeniu.

    # Przykład zgodny z prezentacją zakłada, że wpisana liczba jest sensowna,
    # tj. nie mniejsza od 0 i nie większa od liczby wszystkich zadań.


if __name__ == '__main__':
    przyklad_06_flaga_zaliczenie()  # Uruchom tylko to jedno zadanie.
