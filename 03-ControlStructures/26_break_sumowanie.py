# -*- coding: utf-8 -*-
# Samodzielny przykład nr 26 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 26. BREAK — ZAKOŃCZENIE PĘTLI PO WPISANIU ZERA
# ===========================================================================
def przyklad_26_break_sumowanie():
    """Zbieramy liczby podawane przez użytkownika; zero kończy pętlę."""
    total_sum = 0  # Na początku suma podanych liczb wynosi zero.

    # while True oznacza pętlę bez własnego automatycznego warunku końca.
    # W zwykłych okolicznościach powtarzałaby się ona bez przerwy.
    while True:  # Wchodzimy do pętli, której przerwanie kontroluje break.
        # int() zamienia tekst z input() na liczbę całkowitą.
        number = int(input('Enter number, 0 to stop: '))

        if number == 0:  # Sprawdzamy, czy wpisano wartość kończącą (zero).
            break       # Natychmiast wychodzimy z pętli while.

        # Ten wiersz jest POMIJANY, jeżeli number == 0 uruchomiło break.
        # += dodaje nową liczbę do dotychczasowej sumy.
        total_sum += number  # Aktualizujemy sumę i wracamy na początek pętli.

    print(total_sum)  # Wyświetlamy sumę po wyjściu z pętli.

    # Przykładowa idea: podaj 5, potem 7, potem 0. Suma to 12.
    # Wartość 0 tylko KOŃCZY wczytywanie; nie zmienia sumy.


if __name__ == '__main__':
    przyklad_26_break_sumowanie()  # Uruchom tylko to jedno zadanie.
