# -*- coding: utf-8 -*-
# Samodzielny przykład nr 20 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 20. BUILDING TEXT IN A LOOP — TWORZENIE NOWEGO NAPISU
# ===========================================================================
def przyklad_20_budowanie_napisu():
    """Doklejamy każdy znak i spację do zmiennej wynikowej."""
    university = 'Krakow University of Economics'  # Tekst wejściowy.
    university_expanded = ''  # Pusty napis: jeszcze nic nie zbudowaliśmy.

    # Zmienna char przyjmuje po kolei wszystkie znaki tekstu university.
    for char in university:  # Przetwarzamy litery i oryginalne spacje.
        # = przypisuje nową wartość tej samej zmiennej (nadpisuje starą).
        # + dla napisów ŁĄCZY teksty, nie wykonuje dodawania matematycznego.
        # ' ' to dokładnie jedna spacja dopisywana po każdym znaku.
        university_expanded = university_expanded + char + ' '

    print(university_expanded)  # Pokazujemy cały, stopniowo zbudowany tekst.

    # Oryginalne spacje też są znakami, więc po nich dopisze się kolejna.
    # Po ostatniej literze również powstanie dodatkowa spacja.


if __name__ == '__main__':
    przyklad_20_budowanie_napisu()  # Uruchom tylko to jedno zadanie.
