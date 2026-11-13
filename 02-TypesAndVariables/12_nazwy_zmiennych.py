# -*- coding: utf-8 -*-
# Samodzielny przykład nr 12 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 12. DOBRE NAZWY ZMIENNYCH
# ---------------------------------------------------------------------------
def przyklad_12_nazwy_zmiennych():
    """Przeliczenie km/h na m/s i porównanie czytelności nazw."""
    # SŁABE NAZWY: nie wiadomo, jaką wielkość przechowują x i v.
    x = 70          # x przechowuje prędkość w kilometrach na godzinę.
    v = x / 3.6     # Dzielimy przez 3.6, aby otrzymać metry na sekundę.
    print(v)        # Wyświetlamy wynik obliczenia.

    # DOBRE NAZWY: można od razu odczytać znaczenie przechowywanych danych.
    speed_kmh = 70                # speed_kmh: prędkość w km/h.
    speed_ms = speed_kmh / 3.6    # speed_ms: prędkość w m/s.
    print(speed_ms)               # Wyświetlamy wartość w m/s.
    print(round(speed_ms, 2))     # Zaokrąglamy do dwóch miejsc po przecinku.

    # Dlaczego dzielimy przez 3.6? 1 km = 1000 m, a 1 h = 3600 s.
    # Zatem 1 km/h = 1000/3600 m/s = 1/3.6 m/s.


if __name__ == '__main__':
    przyklad_12_nazwy_zmiennych()  # Uruchom tylko to jedno zadanie.
