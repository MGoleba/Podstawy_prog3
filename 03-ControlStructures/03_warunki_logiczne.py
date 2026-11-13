# -*- coding: utf-8 -*-
# Samodzielny przykład nr 03 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 03. WARUNEK JEST PYTANIEM — TRUE / FALSE
# ===========================================================================
def przyklad_03_warunki_logiczne():
    """Cztery warunki z prezentacji i ich wartości logiczne."""
    # W prezentacji te warunki były zapisane jako niezależne wyrażenia.
    # Tutaj podajemy przykładowe dane, aby dało się je rzeczywiście wykonać.
    car_speed = 150         # Aktualna prędkość auta.
    speed_limit = 140       # Maksymalna prędkość.
    account_balance = 500   # Saldo konta (kwota dostępna do wydania).
    total_payment = 200     # Kwota, którą chcemy zapłacić.
    tasks_ok = 12           # Liczba poprawnie rozwiązanych zadań.
    total_tasks = 20        # Liczba wszystkich zadań.
    number = 8              # Liczba, której parzystość chcemy sprawdzić.

    # > znaczy „większe od”. Wynik porównania ma typ bool: True lub False.
    print(car_speed > speed_limit)  # Pytamy: czy przekroczono prędkość?

    # >= oznacza „większe lub równe”; porównujemy środki z kwotą płatności.
    print(account_balance >= total_payment)  # Czy pieniędzy jest dość?

    # / to dzielenie, np. 20 / 2 = 10; pytamy, czy poprawnych zadań jest >= 10.
    print(tasks_ok >= total_tasks / 2)  # Czy zaliczono co najmniej połowę?

    # % to RESZTA z dzielenia; == sprawdza równość (nie przypisuje wartości).
    # Liczba parzysta daje po podzieleniu przez 2 resztę równą 0.
    print(number % 2 == 0)  # Czy liczba jest parzysta?


if __name__ == '__main__':
    przyklad_03_warunki_logiczne()  # Uruchom tylko to jedno zadanie.
