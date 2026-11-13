# -*- coding: utf-8 -*-
# Samodzielny przykład nr 24 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 24. WHILE LOOP — POWTARZANIE, DOPÓKI WARUNEK JEST TRUE
# ===========================================================================
def przyklad_24_while_licznik():
    """Pętla pokazuje liczby 0–4 i zatrzymuje się, gdy count osiągnie 5."""
    count = 0  # Ustawiamy licznik, aby pętla miała punkt startowy.

    # while znaczy „dopóki”; blok wykonuje się, dopóki count < 5 jest True.
    # Przed każdą następną iteracją Python ponownie sprawdza warunek.
    while count < 5:  # Przy count=5 warunek będzie False i pętla się skończy.
        print(count)  # Pokazujemy bieżącą wartość licznika.
        count += 1    # Zwiększamy licznik o 1, żeby zbliżać się do końca pętli.

    # BEZ count += 1 licznik pozostałby 0 i pętla trwałaby bez końca.
    # Taka sytuacja nazywa się pętlą nieskończoną (infinite loop).


if __name__ == '__main__':
    przyklad_24_while_licznik()  # Uruchom tylko to jedno zadanie.
