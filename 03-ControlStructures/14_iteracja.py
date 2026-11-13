# -*- coding: utf-8 -*-
# Samodzielny przykład nr 14 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 14. ITERATION — CZYM JEST POWTARZANIE INSTRUKCJI?
# ===========================================================================
def przyklad_14_iteracja():
    """Krótki przykład pojęcia iteracji (bez dodatkowych nowych konstrukcji)."""
    # ITERACJA oznacza jedno wykonanie bloku kodu w ramach pętli.
    # Pętle pozwalają przetwarzać wiele elementów bez kopiowania instrukcji.
    # W Pythonie główne typy pętli to for oraz while.
    for number in (10, 20, 30):  # Po kolei bierzemy 10, potem 20, potem 30.
        print(number)  # Ten wiersz wykona się raz dla każdej z trzech wartości.

    # To dodatkowa demonstracja definicji iteracji z prezentacji.


if __name__ == '__main__':
    przyklad_14_iteracja()  # Uruchom tylko to jedno zadanie.
