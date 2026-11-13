# -*- coding: utf-8 -*-
# Samodzielny przykład nr 04 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 4. RÓŻNICA MIĘDZY TRYBEM INTERAKTYWNYM A SKRYPTOWYM
# ---------------------------------------------------------------------------
def przyklad_04_tryby_pracy():
    """To samo działanie w skrypcie; komentarze objaśniają różnicę."""
    # TRYB INTERAKTYWNY:
    # Uruchamiasz interpreter i wpisujesz np. 10 + 20.
    # Interpreter automatycznie pokazuje wynik wyrażenia: 30.
    # Nadaje się do szybkiego sprawdzania małych fragmentów kodu.

    # TRYB SKRYPTOWY:
    # Piszesz kod w pliku zakończonym rozszerzeniem .py.
    # Wyrażenie 10 + 20 samo w sobie nie wyświetli tutaj wyniku.
    # print() pokazuje obliczoną wartość w terminalu.
    print(10 + 20)  # Dodajemy dwie liczby i wyświetlamy sumę.


if __name__ == '__main__':
    przyklad_04_tryby_pracy()  # Uruchom tylko to jedno zadanie.
