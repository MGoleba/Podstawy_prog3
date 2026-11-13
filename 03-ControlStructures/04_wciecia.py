# -*- coding: utf-8 -*-
# Samodzielny przykład nr 04 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 04. WCIĘCIA OKREŚLAJĄ, KTÓRE LINIE NALEŻĄ DO IF
# ===========================================================================
def przyklad_04_wciecia():
    """Dwie linie są w if, jedna jest poza nim."""
    # Wcięcia w Pythonie nie są wyłącznie ozdobą. Decydują o znaczeniu kodu.
    speed_limit = 140  # Definiujemy limit, aby przykład działał samodzielnie.
    car_speed = 150    # Wartość przykładowa, większa od limitu.

    if car_speed > speed_limit:   # Rozpoczynamy blok dla przekroczenia limitu.
        print('Too fast')        # Cztery spacje: jesteśmy wewnątrz bloku if.
        print('Slow down')       # Też cztery spacje: nadal wewnątrz if.

    print('End of speed check')  # Brak wcięcia: wykonuje się ZAWSZE.

    # Jeżeli ustawisz car_speed = 120, dwa komunikaty wewnątrz if znikną.
    # Trzeci komunikat nadal się pojawi, ponieważ NIE należy do bloku if.
    # Nieprawidłowe wcięcie może wywołać IndentationError.


if __name__ == '__main__':
    przyklad_04_wciecia()  # Uruchom tylko to jedno zadanie.
