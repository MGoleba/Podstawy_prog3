# -*- coding: utf-8 -*-
# Samodzielny przykład nr 25 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 25. COMPARISON OPERATORS — OPERATORY PORÓWNANIA
# ---------------------------------------------------------------------------
def przyklad_25_porownania():
    """Porównania ==, !=, >, <, >=, <= zwracają wartości bool."""
    x = 5  # Tworzymy zmienną, której wartość będziemy porównywać.

    print(x == 5)  # == sprawdza, czy wartości są równe.
    print(x != 5)  # != sprawdza, czy wartości są różne.
    print(x > 5)   # > sprawdza, czy lewa liczba jest większa od prawej.
    print(x < 5)   # < sprawdza, czy lewa liczba jest mniejsza od prawej.
    print(x >= 5)  # >= sprawdza, czy lewa jest większa LUB równa prawej.
    print(x <= 5)  # <= sprawdza, czy lewa jest mniejsza LUB równa prawej.

    # Ważne: x = 5 PRZYPISUJE wartość; x == 5 PORÓWNUJE wartości.


if __name__ == '__main__':
    przyklad_25_porownania()  # Uruchom tylko to jedno zadanie.
