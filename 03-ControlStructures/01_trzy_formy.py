# -*- coding: utf-8 -*-
# Samodzielny przykład nr 01 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 01. TRZY PODSTAWOWE SPOSOBY STEROWANIA PROGRAMEM
# ===========================================================================
def przyklad_01_trzy_formy():
    """Kolejność (sequence), wybór (selection), powtarzanie (iteration)."""
    # 1) SEQUENCE (SEKWENCJA): instrukcje po prostu wykonują się w kolejności.
    first_number = 2  # Zapisujemy pierwszą liczbę.
    second_number = 3  # Zapisujemy drugą liczbę.
    print(first_number + second_number)  # Dodajemy je i wyświetlamy sumę.

    # 2) SELECTION (WYBÓR): wykonanie instrukcji zależy od warunku.
    if first_number < second_number:  # Pytamy, czy pierwsza liczba jest mniejsza.
        print('Pierwsza liczba jest mniejsza.')  # Wykonujemy tylko gdy True.

    # 3) ITERATION (POWTARZANIE): pętla wykonuje blok kilka razy.
    # range(2) tworzy wartości 0 i 1; dla każdej wykonamy print().
    for i in range(2):  # Zmienna i kolejno otrzyma 0, a potem 1.
        print('Powtarzam instrukcję.')  # Dwa wykonania tej samej linii.


if __name__ == '__main__':
    przyklad_01_trzy_formy()  # Uruchom tylko to jedno zadanie.
