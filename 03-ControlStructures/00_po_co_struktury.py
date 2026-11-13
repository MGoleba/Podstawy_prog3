# -*- coding: utf-8 -*-
# Samodzielny przykład nr 00 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 00. PO CO SĄ STRUKTURY STERUJĄCE? (WHY CONTROL STRUCTURES MATTER)
# ===========================================================================
def przyklad_00_po_co_struktury():
    """Pokazuje różnicę między działaniem po kolei a wyborem działania."""
    # Program często musi zrobić coś innego w zależności od danych.
    # Gdy instrukcje wykonują się po kolei, mówimy o SEKWENCJI.
    # Gdy instrukcja zależy od warunku, mówimy o WYBORZE / ROZGAŁĘZIENIU.
    # Gdy instrukcja wykonuje się wielokrotnie, mówimy o POWTARZANIU.

    temperature = 10  # Zapisujemy temperaturę w zmiennej; = oznacza przypisanie.
    print('Sprawdzamy temperaturę.')  # Ta linia wykona się zawsze, jako pierwsza.

    # if oznacza „jeśli”. Python sprawdza, czy 10 < 15 jest prawdą.
    # Dwukropek : rozpoczyna blok zależny od warunku.
    if temperature < 15:
        # Wcięcie czterech spacji oznacza, że ta linia należy do if.
        print('Jest chłodno.')  # Wyświetli się tylko wtedy, gdy warunek jest True.

    print('Koniec sprawdzania.')  # Brak wcięcia: to już NIE jest część if.


if __name__ == '__main__':
    przyklad_00_po_co_struktury()  # Uruchom tylko to jedno zadanie.
