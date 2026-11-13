# -*- coding: utf-8 -*-
# Samodzielny przykład nr 12 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 12. DISCOUNT ELIGIBILITY — SPRAWDZENIE PRAWA DO ZNIŻKI
# ===========================================================================
def przyklad_12_znizka_wiek():
    """Zniżka przysługuje osobom poniżej 18 lat LUB od 65 lat."""
    age = int(input('Enter your age: '))  # Wczytujemy wiek jako liczbę całkowitą.

    # < 18 to „mniej niż 18”, a >= 65 to „65 lub więcej”.
    # or oznacza LUB, czyli wystarczy prawdziwość jednego z dwóch warunków.
    if age < 18 or age >= 65:          # Sprawdzamy dwa uprawniające przypadki.
        print('Discount available')  # Zniżka jest dostępna.
    else:  # Użytkownik ma od 18 do 64 lat włącznie.
        print('No discount')  # Zniżka nie jest dostępna w tym przykładzie.

    # Reguła zniżki jest UMOWNA, dokładnie taka jak w prezentacji.
    # Nie oznacza ogólnego przepisu obowiązującego w każdym sklepie.


if __name__ == '__main__':
    przyklad_12_znizka_wiek()  # Uruchom tylko to jedno zadanie.
