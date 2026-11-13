# -*- coding: utf-8 -*-
# Samodzielny przykład nr 19 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 19. WYPISYWANIE NUMERÓW POWTÓRZEŃ
# ===========================================================================
def przyklad_19_licznik_powtorzen():
    """Zmiennej i używamy do wskazania numeru kolejnego powtórzenia."""
    # range(1, 7) daje kolejno: 1, 2, 3, 4, 5, 6 (bez 7).
    for i in range(1, 7):  # i przechowuje numer aktualnej iteracji.
        # f przed cudzysłowem oznacza f-string, czyli tekst ze zmiennymi.
        # {i} zostanie zastąpione aktualną wartością licznika pętli.
        print(f'Repetition {i}')  # Pokazujemy np. Repetition 1, 2 itd.


if __name__ == '__main__':
    przyklad_19_licznik_powtorzen()  # Uruchom tylko to jedno zadanie.
