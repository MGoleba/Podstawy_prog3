# -*- coding: utf-8 -*-
# Samodzielny przykład nr 14 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

import math  # Standardowa biblioteka Pythona.
import random  # Standardowa biblioteka Pythona.

# ---------------------------------------------------------------------------
# 14. MODULES AND FUNCTIONS — MODUŁY I FUNKCJE
# ---------------------------------------------------------------------------
def przyklad_14_moduly_funkcje():
    """Pierwiastek z sumy kwadratów oraz losowanie liczby od 1 do 6."""
    # math i random zostały zaimportowane na początku tego pliku.
    a = 5  # Długość pierwszego boku prostokąta.
    b = 8  # Długość drugiego boku prostokąta.

    # math.sqrt(wartosc) oblicza pierwiastek kwadratowy z wartości.
    # a ** 2 + b ** 2 to suma kwadratów długości dwóch boków.
    # Cały wzór wynika z twierdzenia Pitagorasa: przekątna = sqrt(a² + b²).
    diagonal = math.sqrt(a ** 2 + b ** 2)
    print(diagonal)             # Wyświetlamy dokładniejszy wynik.
    print(round(diagonal, 2))   # Wyświetlamy przekątną z 2 miejscami.

    # random.randint(1, 6) wybiera jedną liczbę całkowitą od 1 do 6.
    dice_roll = random.randint(1, 6)
    print(dice_roll)            # Pokazujemy wylosowaną liczbę.


if __name__ == '__main__':
    przyklad_14_moduly_funkcje()  # Uruchom tylko to jedno zadanie.
