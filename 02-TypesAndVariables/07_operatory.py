# -*- coding: utf-8 -*-
# Samodzielny przykład nr 07 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 7. OPERATORY ARYTMETYCZNE
# ---------------------------------------------------------------------------
def przyklad_07_operatory():
    """Dodawanie, odejmowanie, mnożenie, potęgi i odmiany dzielenia."""
    print(2 + 3)        # + dla liczb oznacza dodawanie.
    print('A' + 'B')    # + dla tekstów (str) łączy napisy w jeden napis.
    print(8 - 3)        # - oznacza odejmowanie.
    print(4 * 5)        # * oznacza mnożenie.
    print(2 ** 3)       # ** oznacza potęgowanie (2 * 2 * 2).
    print(7 / 2)        # / oznacza zwykłe dzielenie; wynik ma typ float.
    print(7 // 2)       # // to dzielenie z zaokrągleniem w dół.
    print(7 % 2)        # % zwraca resztę z dzielenia.
    print(-7 // 2)      # Wynik // zaokrągla w dół, więc tutaj otrzymamy -4.

    # Nie myl ** z ^. Znak ^ w Pythonie ma inne znaczenie (XOR bitowy).
    # Działanie 7 % 2 daje resztę 1, bo 7 = 3 * 2 + 1.


if __name__ == '__main__':
    przyklad_07_operatory()  # Uruchom tylko to jedno zadanie.
