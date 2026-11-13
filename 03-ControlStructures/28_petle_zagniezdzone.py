# -*- coding: utf-8 -*-
# Samodzielny przykład nr 28 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 28. NESTED LOOPS — PĘTLA W PĘTLI
# ===========================================================================
def przyklad_28_petle_zagniezdzone():
    """Wypisujemy dziewięć par (wiersz, kolumna) w układzie 3 × 3."""
    # Zewnętrzna pętla wybiera kolejny wiersz: 1, 2, potem 3.
    for row in range(1, 4):  # row = 1, 2, 3; górna granica 4 jest pominięta.
        # Dla KAŻDEGO wiersza wykonujemy wewnętrzną pętlę od nowa.
        for col in range(1, 4):  # col = 1, 2, 3 dla każdej wartości row.
            # print(a, b) wyświetla dwie liczby, domyślnie ze spacją między nimi.
            print(row, col)  # Kolejno (1,1), (1,2), ... aż do (3,3).

    # Zewnętrzna pętla ma 3 iteracje, wewnętrzna po 3 w każdej z nich.
    # Łącznie instrukcja print() wykona się 3 × 3 = 9 razy.


if __name__ == '__main__':
    przyklad_28_petle_zagniezdzone()  # Uruchom tylko to jedno zadanie.
