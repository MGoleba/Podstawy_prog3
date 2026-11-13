# -*- coding: utf-8 -*-
# Samodzielny przykład nr 13 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 13. ASSIGNMENT — PRZYPISYWANIE WARTOŚCI
# ---------------------------------------------------------------------------
def przyklad_13_przypisanie():
    """Aktualizacja zmiennej: x = x + 1."""
    x = 7          # Tworzymy zmienną x o wartości 7.
    x = x + 1      # Najpierw liczymy prawą stronę: 7 + 1 = 8.
                   # Dopiero potem nadpisujemy starą wartość x liczbą 8.
    print(x)       # Wyświetlamy nową wartość zmiennej.

    x += 1         # Skrócona postać x = x + 1; zwiększamy x o 1.
    print(x)       # Wyświetlamy wartość po kolejnym zwiększeniu.

    # = oznacza PRZYPISANIE, a == oznacza PORÓWNANIE RÓWNOŚCI.


if __name__ == '__main__':
    przyklad_13_przypisanie()  # Uruchom tylko to jedno zadanie.
