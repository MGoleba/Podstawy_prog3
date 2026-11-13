# -*- coding: utf-8 -*-
# Samodzielny przykład nr 29 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 29. FROM TASK TO PROGRAM — KOSZT PALIWA NA TRASIE
# ---------------------------------------------------------------------------
def przyklad_29_koszt_transportu():
    """Obliczamy zużycie paliwa i jego koszt na podstawie trzech danych."""
    # distance oznacza długość trasy w kilometrach.
    # int() zamienia wpisany tekst na liczbę całkowitą.
    distance = int(input('Distance: '))

    # fuel_price oznacza cenę jednego litra paliwa.
    # float() pozwala na część dziesiętną, np. 6.5.
    fuel_price = float(input('Fuel price: '))

    # consumption oznacza średnie spalanie w litrach na 100 km.
    consumption = float(input('L/100 km: '))

    # Najpierw mnożymy długość trasy przez spalanie.
    # Dzielenie przez 100 jest konieczne, bo spalanie podano NA 100 km.
    # Wynik fuel oznacza liczbę potrzebnych litrów paliwa.
    fuel = distance * consumption / 100

    # Koszt paliwa = liczba zużytych litrów * cena jednego litra.
    cost = fuel * fuel_price

    # :.2f pokazuje koszt z dokładnie dwoma miejscami po kropce.
    print(f'Cost: {cost:.2f}')

    # Program liczy tylko koszt zużytego paliwa.
    # Nie uwzględnia opłat drogowych, amortyzacji pojazdu itp.


if __name__ == '__main__':
    przyklad_29_koszt_transportu()  # Uruchom tylko to jedno zadanie.
