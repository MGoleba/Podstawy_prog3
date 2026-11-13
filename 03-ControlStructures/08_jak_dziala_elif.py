# -*- coding: utf-8 -*-
# Samodzielny przykład nr 08 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 08. WIELE MOŻLIWYCH GAŁĘZI — IF / ELIF / ELSE
# ===========================================================================
def przyklad_08_jak_dziala_elif():
    """Przykład demonstracyjny zamiast ogólnego schematu condition1/2/3."""
    # Prezentacja podaje schemat z „condition1”, „condition2” i „condition3”.
    # To nazwy umowne, a nie gotowy działający program. Poniżej wersja
    # uruchamialna pokazująca dokładnie tę samą zasadę.
    points = 75  # Wynik punktowy użyty wyłącznie do demonstracji.

    # Python sprawdza kolejne warunki, dopóki nie znajdzie pierwszego True.
    if points >= 90:  # Pierwsza możliwość: wynik co najmniej 90 punktów.
        print('Wynik bardzo wysoki.')  # Wykona się tylko dla points >= 90.
    elif points >= 70:  # „W przeciwnym razie, jeśli” wynik >= 70.
        print('Wynik dobry.')         # Dla 75 punktów wykona się ta gałąź.
    elif points >= 50:  # Sprawdzane tylko jeśli dwa wcześniejsze były False.
        print('Wynik dostateczny.')  # Nie wykona się dla 75 punktów.
    else:  # Jeśli ŻADEN z warunków if/elif nie był prawdziwy.
        print('Wynik poniżej progu.')  # Obsługa pozostałych przypadków.

    # Z łańcucha if/elif/else wykonuje się TYLKO jedna pasująca gałąź.
    # Kolejność sprawdzania ma znaczenie: zwykle zaczynamy od najwyższego progu.


if __name__ == '__main__':
    przyklad_08_jak_dziala_elif()  # Uruchom tylko to jedno zadanie.
