# -*- coding: utf-8 -*-
# Samodzielny przykład nr 13 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 13. NESTED DECISIONS — ZAGNIEŻDŻONE IF, SPRAWDZENIE DNIA LUTEGO
# ===========================================================================
def przyklad_13_zagniezdzone_if():
    """Wewnętrzny if wykonuje się tylko po spełnieniu zewnętrznego if."""
    month = int(input('Month: '))  # Pobieramy numer miesiąca jako liczbę.
    day = int(input('Day: '))      # Pobieramy dzień miesiąca jako liczbę.

    day_ok = False  # Na początku zakładamy, że podany dzień jest niepoprawny.

    if month == 2:  # == pyta, czy podano drugi miesiąc, czyli luty.
        # Dopiero jeśli miesiąc to luty, sprawdzamy numer dnia.
        # and wymaga spełnienia OBU warunków: dzień >= 1 oraz dzień <= 28.
        if day >= 1 and day <= 28:  # Wcięcie 8 spacji: if wewnątrz innego if.
            day_ok = True  # Ustawiamy flagę na True tylko dla dni 1–28 lutego.

    # Wynik dodany, by dało się zobaczyć wartość flagi po wykonaniu ćwiczenia.
    print('Day valid in simplified February check:', day_ok)

    # ISTOTNE: przykład odpowiada TYLKO na pytanie „czy to dzień od 1 do 28
    # lutego?”. Dla stycznia zwróci False, choć może to być poprawna data.
    # Nie uwzględnia również 29 lutego w latach przestępnych.


if __name__ == '__main__':
    przyklad_13_zagniezdzone_if()  # Uruchom tylko to jedno zadanie.
