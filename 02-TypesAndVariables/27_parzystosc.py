# -*- coding: utf-8 -*-
# Samodzielny przykład nr 27 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 27. REMAINDER AND EVEN NUMBERS — SPRAWDZANIE PARZYSTOŚCI
# ---------------------------------------------------------------------------
def przyklad_27_parzystosc():
    """Liczba całkowita jest parzysta, gdy liczba % 2 == 0."""
    # % zwraca resztę z dzielenia, a NIE procent wartości.
    print(7 % 2)  # Siedem dzielone przez dwa daje resztę 1.
    print(8 % 2)  # Osiem dzielone przez dwa daje resztę 0.

    # Wczytujemy dane i od razu zamieniamy tekst na liczbę całkowitą.
    number = int(input('Enter number: '))

    # Najpierw number % 2 oblicza resztę z dzielenia przez 2.
    # Następnie == 0 sprawdza, czy reszta wyniosła zero.
    # Wynik jest bool i zostaje zapisany do zmiennej even („parzysta”).
    even = number % 2 == 0

    # F-string wstawia wartość True albo False do komunikatu.
    print(f'Number is even: {even}')


if __name__ == '__main__':
    przyklad_27_parzystosc()  # Uruchom tylko to jedno zadanie.
