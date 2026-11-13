# -*- coding: utf-8 -*-
# Samodzielny przykład nr 25 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 25. ASKING UNTIL INPUT IS CORRECT — PYTANIE O IMIĘ AŻ DO ODPOWIEDZI
# ===========================================================================
def przyklad_25_while_imie():
    """Powtarzamy pytanie, dopóki użytkownik podaje pusty tekst."""
    name = ''  # Pusty napis: jeszcze nie znamy imienia użytkownika.

    # == '' oznacza „jest dokładnie pustym napisem” (zero znaków).
    while name == '':  # Jeśli użytkownik nic nie wpisze, wracamy do pytania.
        name = input('Enter your name: ')  # Pobieramy imię i nadpisujemy name.

    # Ten print jest POZA pętlą, więc wykona się dopiero po niepustej odpowiedzi.
    print(f'Hello {name}')  # Wstawiamy wpisane imię do komunikatu.

    # Ważne: tekst '   ' (same spacje) NIE jest pusty według warunku z prezentacji.
    # Bardziej restrykcyjny wariant użyłby name.strip() == '', ale w tym
    # zadaniu zachowujemy dokładnie sposób działania podany w materiałach.


if __name__ == '__main__':
    przyklad_25_while_imie()  # Uruchom tylko to jedno zadanie.
