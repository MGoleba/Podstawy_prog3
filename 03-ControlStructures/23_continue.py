# -*- coding: utf-8 -*-
# Samodzielny przykład nr 23 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 23. CONTINUE — POMIJANIE RESZTY BIEŻĄCEJ ITERACJI
# ===========================================================================
def przyklad_23_continue():
    """Ta sama suma parzystych; tym razem pomijamy nieparzyste przez continue."""
    total = 0  # Ustawiamy sumę początkową na zero.

    for i in range(1, 11):  # Przechodzimy przez liczby od 1 do 10.
        # != oznacza „różne od”, więc i % 2 != 0 rozpoznaje nieparzyste.
        if i % 2 != 0:  # Jeśli bieżąca liczba jest NIEPARZYSTA...
            continue    # ...pomijamy resztę tej iteracji i bierzemy kolejną i.

        # Ta linia wykona się tylko dla liczb parzystych.
        # Dla nieparzystych polecenie continue przeskoczy ją całkowicie.
        total += i  # Dodajemy aktualną liczbę parzystą do sumy.

    print(total)  # Otrzymujemy ten sam wynik co w poprzednim przykładzie: 30.

    # continue NIE kończy całej pętli. Kończy tylko bieżącą iterację.
    # Całą pętlę przerwalibyśmy instrukcją break (pokazana dalej).


if __name__ == '__main__':
    przyklad_23_continue()  # Uruchom tylko to jedno zadanie.
