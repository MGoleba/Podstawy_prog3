# -*- coding: utf-8 -*-
# Samodzielny przykład nr 20 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 20. STRINGS AS SEQUENCES — DŁUGOŚĆ TEKSTU I INDEKSY
# ---------------------------------------------------------------------------
def przyklad_20_znaki_indeksy():
    """Funkcja len() i wybieranie znaków przez nawiasy kwadratowe []."""
    name = 'Anna'      # Tworzymy czteroznakowy napis.
    print(len(name))   # len() podaje liczbę znaków, wliczając spacje.

    # Indeksowanie w Pythonie rozpoczyna się od 0, a nie od 1.
    # Dla 'Anna': A ma indeks 0, n indeks 1, n indeks 2, a indeks 3.
    print(name[0])    # Pobieramy pierwszy znak (o indeksie 0).
    print(name[1])    # Pobieramy drugi znak (o indeksie 1).
    print(name[3])    # Pobieramy czwarty i ostatni znak (indeks 3).

    # print(name[4])  # BŁĄD: nie istnieje znak o indeksie 4 (IndexError).


if __name__ == '__main__':
    przyklad_20_znaki_indeksy()  # Uruchom tylko to jedno zadanie.
