# -*- coding: utf-8 -*-
# Samodzielny przykład nr 06 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 6. EXPRESSIONS AND VALUES — WYRAŻENIA I WARTOŚCI
# ---------------------------------------------------------------------------
def przyklad_06_wyrazenia():
    """Wyrażenie to fragment kodu, którego wykonanie daje wartość."""
    # * oznacza mnożenie; mnożenie ma pierwszeństwo przed dodawaniem.
    print(3 * 2 + 1)  # Najpierw 3 * 2, a potem + 1.

    # Tutaj również najpierw mnożymy, a następnie dodajemy.
    print(5 + 10 * 5)

    # True i False to wartości logiczne: prawda i fałsz (typ bool).
    # != oznacza „nie jest równe”, czyli porównanie różności.
    print(True != False)  # Sprawdzamy, czy prawda jest różna od fałszu.


if __name__ == '__main__':
    przyklad_06_wyrazenia()  # Uruchom tylko to jedno zadanie.
