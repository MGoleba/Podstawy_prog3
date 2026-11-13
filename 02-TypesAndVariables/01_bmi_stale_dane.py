# -*- coding: utf-8 -*-
# Samodzielny przykład nr 01 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 1. PODSTAWOWA IDEA PROGRAMOWANIA — OBLICZANIE BMI
# ---------------------------------------------------------------------------
def przyklad_01_bmi_stale_dane():
    """Obliczanie BMI dla podanej w kodzie masy i wzrostu."""
    weight = 77   # weight = masa ciała w kilogramach; znak = przypisuje wartość.
    height = 180  # height = wzrost w centymetrach (nie w metrach).

    # Najpierw height / 100 zamienia centymetry na metry: 180 / 100 = 1.8.
    # Potem mnożymy wzrost w metrach przez siebie: 1.8 * 1.8 = 3.24.
    # Następnie dzielimy masę przez kwadrat wzrostu: 77 / 3.24.
    # Wynik zapisujemy pod nową nazwą bmi.
    bmi = weight / ((height / 100) * (height / 100))

    print(bmi)  # Wyświetlamy niezaokrągloną wartość zmiennej bmi.
    # round(liczba, 2) zaokrągla liczbę do maksymalnie 2 miejsc po przecinku.
    print(round(bmi, 2))  # Wyświetlamy wygodniejszą do odczytania wersję.


if __name__ == '__main__':
    przyklad_01_bmi_stale_dane()  # Uruchom tylko to jedno zadanie.
