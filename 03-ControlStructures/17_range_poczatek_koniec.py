# -*- coding: utf-8 -*-
# Samodzielny przykład nr 17 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 17. RANGE(START, STOP) — LICZBY OD 1 DO 5
# ===========================================================================
def przyklad_17_range_poczatek_koniec():
    """Dwa argumenty zakresu: start włączony, stop wyłączony."""
    # range(1, 6) oznacza wartości 1, 2, 3, 4, 5.
    # 1 jest uwzględniona, ale 6 już NIE.
    for i in range(1, 6):  # Rozpoczynamy od 1, kończymy przed 6.
        print(i)           # Wyświetlamy kolejne wartości pętli.


if __name__ == '__main__':
    przyklad_17_range_poczatek_koniec()  # Uruchom tylko to jedno zadanie.
