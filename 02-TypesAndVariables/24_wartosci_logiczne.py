# -*- coding: utf-8 -*-
# Samodzielny przykład nr 24 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 24. LOGICAL VALUES — WARTOŚCI TRUE I FALSE
# ---------------------------------------------------------------------------
def przyklad_24_wartosci_logiczne():
    """Sprawdzamy sam warunek wieku, bez wyciągania wniosków podatkowych."""
    age = 22  # Wiek zapisujemy jako liczbę całkowitą.

    # <= oznacza „mniejsze lub równe”.
    # age <= 26 sprawdza jedynie, czy wiek nie przekracza 26 lat.
    # Wynikiem jest wartość logiczna: True albo False.
    no_tax = age <= 26  # Taka nazwa pojawia się w prezentacji.
    print(no_tax)        # Wyświetlamy wynik sprawdzenia warunku.

    # UWAGA: nazwa no_tax jest tutaj tylko nazwą ćwiczeniową.
    # Sam warunek wieku NIE ustala, czy dana osoba płaci podatek.


if __name__ == '__main__':
    przyklad_24_wartosci_logiczne()  # Uruchom tylko to jedno zadanie.
