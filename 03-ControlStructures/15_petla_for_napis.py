# -*- coding: utf-8 -*-
# Samodzielny przykład nr 15 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 15. FOR LOOP — PRZECHODZENIE PO ZNAKACH NAPISU
# ===========================================================================
def przyklad_15_petla_for_napis():
    """Pętla for pobiera kolejno każdy znak ze zmiennej city."""
    city = 'Krakow'  # Tworzymy napis, czyli wartość typu str.

    # for oznacza „dla każdego”; char to bieżący znak tekstu.
    # in oznacza pobieranie kolejnych elementów z city.
    # Dwukropek rozpoczyna blok, którego wcięcie wynosi 4 spacje.
    for char in city:  # Najpierw char='K', potem 'r', 'a', 'k', 'o', 'w'.
        print(char)    # Każdą literę drukujemy w osobnym wierszu.

    # Zmienna char ma nową wartość przy każdym obrocie pętli.
    # Pętla zakończy się sama po przetworzeniu ostatniego znaku.


if __name__ == '__main__':
    przyklad_15_petla_for_napis()  # Uruchom tylko to jedno zadanie.
