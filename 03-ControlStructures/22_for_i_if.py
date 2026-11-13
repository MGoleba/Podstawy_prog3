# -*- coding: utf-8 -*-
# Samodzielny przykład nr 22 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 22. COMBINING LOOP AND DECISION — SUMA LICZB PARZYSTYCH OD 1 DO 10
# ===========================================================================
def przyklad_22_for_i_if():
    """Dodajemy wyłącznie te liczby, których reszta z dzielenia przez 2 = 0."""
    total = 0  # Zmienna zbierająca sumę; początkowo nie zawiera żadnej sumy.

    # range(1, 11) to liczby od 1 do 10 włącznie.
    for i in range(1, 11):  # Pętla wykonuje 10 iteracji.
        # Wcięcie 4 spacji: ten if należy do pętli for.
        if i % 2 == 0:  # % wyznacza resztę; == 0 oznacza parzystość.
            # Wcięcie 8 spacji: dodajemy tylko przy prawdziwym warunku if.
            total += i  # To skrót zapisu total = total + i.

    print(total)  # Końcowa suma to 2 + 4 + 6 + 8 + 10 = 30.


if __name__ == '__main__':
    przyklad_22_for_i_if()  # Uruchom tylko to jedno zadanie.
