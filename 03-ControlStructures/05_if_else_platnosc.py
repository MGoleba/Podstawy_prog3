# -*- coding: utf-8 -*-
# Samodzielny przykład nr 05 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 05. IF / ELSE — PŁATNOŚĆ Z KONTA
# ===========================================================================
def przyklad_05_if_else_platnosc():
    """Program wybiera jedną z dwóch możliwych odpowiedzi."""
    account_balance = 500  # Saldo na rachunku wynosi 500.

    # input() zwraca tekst; int() zamienia go na liczbę całkowitą.
    total_payment = int(input('Payment amount: '))  # Użytkownik podaje kwotę.

    # <= oznacza „mniejsze lub równe”. Równość też oznacza dostępne środki.
    if total_payment <= account_balance:  # Jeśli kwota nie przekracza salda...
        print('Payment completed')        # ...pokazujemy potwierdzenie.
    else:                                 # W przeciwnym razie, gdy if jest False...
        print('No funds')                # ...informujemy o braku środków.

    # else NIE ma własnego warunku. Uruchamia się przy fałszywym if.
    # W jednym wykonaniu tego if/else zostanie wybrana tylko jedna gałąź.
    # To uproszczona symulacja: nie aktualizuje salda i nie obsługuje przelewów.


if __name__ == '__main__':
    przyklad_05_if_else_platnosc()  # Uruchom tylko to jedno zadanie.
