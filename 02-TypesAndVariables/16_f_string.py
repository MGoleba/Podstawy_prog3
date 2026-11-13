# -*- coding: utf-8 -*-
# Samodzielny przykład nr 16 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 16. F-STRINGS — WSTAWIANIE WARTOŚCI ZMIENNYCH DO TEKSTU
# ---------------------------------------------------------------------------
def przyklad_16_f_string():
    """Tworzenie czytelnych komunikatów z użyciem f'...{zmienna}...'."""
    name = 'Adam'  # Imię przechowujemy jako tekst typu str.
    age = 19       # Wiek zapisujemy jako liczbę int.
    height = 180   # Wzrost w centymetrach zapisujemy jako liczbę int.

    # Litera f przed cudzysłowem włącza mechanizm f-string.
    # W nawiasach klamrowych { } umieszczamy zmienne lub całe obliczenia.
    print(f'My name is {name}.')
    print(f'I am {age} years old, and my height is {height} cm.')
    print(f'In 6 years I will be {age + 6} years old.')

    # W trzeciej linijce Python najpierw oblicza age + 6, a potem wstawia wynik.
    # Bez litery f napis {age} zostałby wyświetlony dosłownie jako tekst.


if __name__ == '__main__':
    przyklad_16_f_string()  # Uruchom tylko to jedno zadanie.
