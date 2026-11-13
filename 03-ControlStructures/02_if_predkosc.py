# -*- coding: utf-8 -*-
# Samodzielny przykład nr 02 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 02. INSTRUKCJA WARUNKOWA IF — KONTROLA PRĘDKOŚCI
# ===========================================================================
def przyklad_02_if_predkosc():
    """Ostrzeżenie zostaje pokazane tylko po przekroczeniu limitu."""
    # speed_limit to ograniczenie prędkości podane w km/h.
    speed_limit = 140  # Przypisujemy do zmiennej liczbę całkowitą 140.

    # input() wyświetla pytanie i odczytuje wpis użytkownika jako TEKST.
    # int() zamienia ten tekst np. '150' na liczbę całkowitą 150.
    car_speed = int(input('Enter car speed: '))  # Pobieramy prędkość samochodu.

    # if znaczy „jeśli”; > znaczy „większe niż”.
    # Sprawdzamy, czy prędkość auta jest większa od dozwolonej prędkości.
    if car_speed > speed_limit:  # Kod poniżej wykona się wyłącznie gdy True.
        print('Warning: speed limit exceeded!')  # Wyświetlamy ostrzeżenie.

    # Przy prędkości równej 140 warunek 140 > 140 jest FAŁSZYWY.
    # W takim przypadku komunikat ostrzegawczy w ogóle się nie pojawi.
    # To poprawne: przekroczenie oznacza „więcej niż”, a nie „co najmniej”.


if __name__ == '__main__':
    przyklad_02_if_predkosc()  # Uruchom tylko to jedno zadanie.
