# -*- coding: utf-8 -*-
# Samodzielny przykład nr 02 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 2. INTERACTIVE MODE — OBLICZENIA W TRYBIE INTERAKTYWNYM
# ---------------------------------------------------------------------------
def przyklad_02_tryb_interaktywny():
    """Pokazujemy obliczenia, które można też wpisywać po znaku >>>."""
    # Tryb interaktywny to okno interpretera, w którym Python od razu
    # wyświetla wynik wpisanego wyrażenia, np. po wpisaniu: 7 + 4.
    # Znaki >>> są zachętą interpretera: NIE są częścią wpisywanego kodu.
    # W zwykłym pliku .py używamy print(), żeby wyniki były widoczne.
    print(7 + 4)   # + dodaje liczby 7 oraz 4.
    print(2 ** 3)  # ** oznacza potęgowanie: 2 do potęgi 3.
    print(7 > 5)   # > sprawdza „większe niż”; wynikiem jest True lub False.
    print(7 < 5)   # < sprawdza „mniejsze niż”.


if __name__ == '__main__':
    przyklad_02_tryb_interaktywny()  # Uruchom tylko to jedno zadanie.
