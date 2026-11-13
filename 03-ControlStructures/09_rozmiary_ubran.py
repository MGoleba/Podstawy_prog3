# -*- coding: utf-8 -*-
# Samodzielny przykład nr 09 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 09. EXAMPLE: CLOTHING SIZE — ROZPOZNAWANIE ROZMIARU ODZIEŻY
# ===========================================================================
def przyklad_09_rozmiary_ubran():
    """Tłumaczenie symbolu rozmiaru S/M/L/XL lub zgłoszenie błędu."""
    size = input('Enter size symbol: ')  # Pobieramy tekst, np. 'M' albo 'XL'.

    # == oznacza porównanie tekstów. Wielkie i małe litery są różne:
    # 's' NIE jest równe 'S'. Prezentacja sprawdza dokładnie wielkie symbole.
    if size == 'S':                # Jeśli wpisano dokładnie literę S...
        print('Small size')       # ...wyświetlamy „mały rozmiar”.
    elif size == 'M':              # Jeśli NIE S, ale wpisano M...
        print('Medium size')      # ...wyświetlamy „średni rozmiar”.
    elif size == 'L':              # Jeśli NIE S/M, ale wpisano L...
        print('Large size')       # ...wyświetlamy „duży rozmiar”.
    elif size == 'XL':             # Jeśli NIE S/M/L, ale wpisano XL...
        print('Extra large size') # ...wyświetlamy „bardzo duży rozmiar”.
    else:                          # Każdy inny wpis, np. 'ABC' albo 's'.
        print('Incorrect symbol') # Informujemy, że symbol jest nieprawidłowy.


if __name__ == '__main__':
    przyklad_09_rozmiary_ubran()  # Uruchom tylko to jedno zadanie.
