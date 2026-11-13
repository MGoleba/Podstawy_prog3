# -*- coding: utf-8 -*-
# Samodzielny przykład nr 05 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

import random  # Standardowa biblioteka Pythona.

# ---------------------------------------------------------------------------
# 5. SYMULATOR PIĘCIU RZUTÓW KOSTKĄ
# ---------------------------------------------------------------------------
def przyklad_05_kostka():
    """Pętla for i losowanie liczb z przedziału od 1 do 6."""
    # Moduł random został zaimportowany na początku pliku.
    print('Dice rolling simulator')  # Wyświetlamy tytuł ćwiczenia.

    # for rozpoczyna pętlę, czyli wielokrotne wykonanie tego samego bloku.
    # i to zmienna sterująca; będzie kolejno równa 0, 1, 2, 3 i 4.
    # range(5) podaje 5 wartości, dlatego pętla wykona się 5 razy.
    # in oznacza pobieranie kolejnych wartości z zakresu.
    # Dwukropek : rozpoczyna blok, a wcięcie wskazuje jego instrukcje.
    for i in range(5):
        # random.randint(1, 6) losuje CAŁKOWITĄ liczbę od 1 do 6 włącznie.
        # Kropka między random i randint oznacza wywołanie funkcji z modułu.
        dice_roll = random.randint(1, 6)  # Zapisujemy jeden wylosowany wynik.
        # end=' ' zastępuje domyślny znak nowej linii jedną spacją.
        # Dzięki temu pięć wyników pojawi się obok siebie.
        print(dice_roll, end=' ')

    print()  # Po zakończeniu pętli przechodzimy do nowej linii.


if __name__ == '__main__':
    przyklad_05_kostka()  # Uruchom tylko to jedno zadanie.
