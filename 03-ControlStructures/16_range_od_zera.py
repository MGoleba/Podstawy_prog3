# -*- coding: utf-8 -*-
# Samodzielny przykład nr 16 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 16. RANGE(5) — LICZBY OD 0 DO 4
# ===========================================================================
def przyklad_16_range_od_zera():
    """range(5) podaje pięć wartości zaczynając od zera."""
    # range(5) to zakres 0, 1, 2, 3, 4.
    # Górna granica 5 NIE jest uwzględniona.
    # i to nazwa zmiennej sterującej pętlą; można użyć innej nazwy.
    for i in range(5):  # Uruchamiamy blok 5 razy.
        print(i)        # Pokazujemy obecną wartość i.


if __name__ == '__main__':
    przyklad_16_range_od_zera()  # Uruchom tylko to jedno zadanie.
