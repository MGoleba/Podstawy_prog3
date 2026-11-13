# -*- coding: utf-8 -*-
# Samodzielny przykład nr 21 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 21. SLICING — WYCINANIE FRAGMENTÓW TEKSTU
# ---------------------------------------------------------------------------
def przyklad_21_wycinki_tekstu():
    """Odczytujemy imię, nazwisko i datę urodzenia z dłuższego napisu."""
    employee = 'Mr. John May, born on 1998-02-16'  # Cały opis pracownika.

    # tekst[a:b] zwraca znaki od indeksu a do indeksu b - 1.
    # Indeks końcowy b NIE jest uwzględniany.
    print(employee[4:8])    # Znaki 4, 5, 6, 7, czyli imię John.
    print(employee[9:12])   # Znaki 9, 10, 11, czyli nazwisko May.

    # Ujemne indeksy liczone są od końca: -1 oznacza ostatni znak.
    # [-10:] oznacza „weź ostatnich dziesięć znaków aż do końca napisu”.
    print(employee[-10:])   # Odczytujemy datę urodzenia 1998-02-16.

    word = 'Python'         # Dodatkowy krótki napis pokazujący wycinek.
    print(word[0:3])       # Pobieramy znaki 0, 1 i 2 (bez znaku 3).


if __name__ == '__main__':
    przyklad_21_wycinki_tekstu()  # Uruchom tylko to jedno zadanie.
