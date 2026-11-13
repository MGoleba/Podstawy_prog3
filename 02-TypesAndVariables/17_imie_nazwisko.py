# -*- coding: utf-8 -*-
# Samodzielny przykład nr 17 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 17. INPUT DATA — POBIERANIE IMIENIA I NAZWISKA
# ---------------------------------------------------------------------------
def przyklad_17_imie_nazwisko():
    """Pobieramy dwa napisy, łączymy je ze spacją i wyświetlamy całość."""
    first_name = input('Enter your first name: ')  # Pobieramy imię jako str.
    last_name = input('Enter your last name: ')    # Pobieramy nazwisko jako str.

    # Dla napisów + oznacza ich łączenie; ' ' to pojedyncza spacja.
    # Spację wstawiamy po to, by nie powstał tekst w rodzaju AdamKowalski.
    full_name = first_name + ' ' + last_name

    # {full_name} zostaje zastąpione przez zawartość złączonego tekstu.
    print(f'Your full name is {full_name}')


if __name__ == '__main__':
    przyklad_17_imie_nazwisko()  # Uruchom tylko to jedno zadanie.
