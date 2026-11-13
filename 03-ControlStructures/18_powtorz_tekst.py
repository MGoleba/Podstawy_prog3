# -*- coding: utf-8 -*-
# Samodzielny przykład nr 18 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 18. REPEATING AN INSTRUCTION — SZEŚCIOKROTNE POWTÓRZENIE NAPISU
# ===========================================================================
def przyklad_18_powtorz_tekst():
    """Wypisujemy ten sam napis sześć razy bez kopiowania linijki."""
    # range(6) ma 6 wartości: 0–5, więc pętla wykona się dokładnie 6 razy.
    # Zmienna i nie jest tu wykorzystywana w treści napisu.
    for i in range(6):  # Jedna iteracja dla każdej wartości zakresu.
        print('Practice makes perfect!')  # W każdej iteracji ten sam tekst.


if __name__ == '__main__':
    przyklad_18_powtorz_tekst()  # Uruchom tylko to jedno zadanie.
