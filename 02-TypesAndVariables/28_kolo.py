# -*- coding: utf-8 -*-
# Samodzielny przykład nr 28 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

import math  # Standardowa biblioteka Pythona.

# ---------------------------------------------------------------------------
# 28. ALGORITHM — POLE I OBWÓD KOŁA
# ---------------------------------------------------------------------------
def przyklad_28_kolo():
    """Przekładamy algorytm z prezentacji na działający kod Python."""
    # Kolejne kroki algorytmu: promień -> pi -> pole -> obwód -> wyświetlenie.
    # W prezentacji r jest promieniem koła, a pi stałą matematyczną.
    r = 5  # Przykładowy promień; liczba nie musi pochodzić z input().

    # math.pi zawiera matematyczną stałą pi.
    # Pole koła obliczamy ze wzoru: pi * r do kwadratu.
    area = math.pi * r ** 2

    # Obwód koła obliczamy ze wzoru: 2 * pi * r.
    circumference = 2 * math.pi * r

    # W formatowaniu f-string :.2f zapewnia dwie cyfry po kropce.
    print(f'Pole koła: {area:.2f}')
    print(f'Obwód koła: {circumference:.2f}')

    # Gdy promień podano w cm, pole jest w cm², a obwód w cm.


if __name__ == '__main__':
    przyklad_28_kolo()  # Uruchom tylko to jedno zadanie.
