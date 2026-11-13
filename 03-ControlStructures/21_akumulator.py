# -*- coding: utf-8 -*-
# Samodzielny przykład nr 21 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 21. ACCUMULATOR PATTERN — SUMOWANIE LICZB 1, 2, 3, 4, 5
# ===========================================================================
def przyklad_21_akumulator():
    """Akumulator przechowuje sumę, którą zwiększamy w kolejnych iteracjach."""
    total = 0  # Zaczynamy od zera; nie dodaliśmy jeszcze żadnej liczby.

    # range(1, 6) podaje liczby 1, 2, 3, 4, 5.
    for i in range(1, 6):  # Przechodzimy kolejno przez podane wartości.
        # Najpierw odczytujemy starą wartość total.
        # Dodajemy do niej aktualną wartość i.
        # Następnie nową sumę zapisujemy ponownie do total.
        total = total + i  # Kolejno suma wynosi 1, 3, 6, 10, 15.

    print(f'Sum is {total}')  # Pokazujemy końcową sumę: 15.

    # Zapis total += i jest równoważny instrukcji total = total + i.
    # Przy skróconym zapisie też modyfikujemy istniejącą wartość zmiennej.


if __name__ == '__main__':
    przyklad_21_akumulator()  # Uruchom tylko to jedno zadanie.
