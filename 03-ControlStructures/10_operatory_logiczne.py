# -*- coding: utf-8 -*-
# Samodzielny przykład nr 10 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 10. OPERATORY LOGICZNE AND / OR / NOT
# ===========================================================================
def przyklad_10_operatory_logiczne():
    """Wyjaśnienie trzech operatorów logicznych na przykładach z prezentacji."""
    age = 25  # Przykładowy wiek do obliczeń logicznych.
    password_ok = False  # Zmienna typu bool: hasło w tym przykładzie jest błędne.

    # and oznacza „ORAZ”: OBA warunki muszą być prawdziwe.
    # Wiek 25 jest >= 18 oraz <= 64, więc całe wyrażenie jest True.
    print(age >= 18 and age <= 64)  # Czy wiek mieści się od 18 do 64 włącznie?

    # or oznacza „LUB”: wystarczy co najmniej jeden spełniony warunek.
    # Wiek 25 nie jest < 18 i nie jest >= 65, więc wynik będzie False.
    print(age < 18 or age >= 65)  # Czy użytkownik ma mniej niż 18 albo >= 65?

    # not oznacza „NIE”: odwraca wartość logiczną True <-> False.
    print(not password_ok)  # Skoro password_ok=False, to not daje True.

    # Ważne: operator or w Pythonie nie wymaga spełnienia obu warunków.
    # and nadaje się np. do sprawdzenia przedziału, or do alternatyw.


if __name__ == '__main__':
    przyklad_10_operatory_logiczne()  # Uruchom tylko to jedno zadanie.
