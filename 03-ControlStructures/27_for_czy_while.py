# -*- coding: utf-8 -*-
# Samodzielny przykład nr 27 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 27. FOR OR WHILE? — JAK DOBRAĆ ODPOWIEDNIĄ PĘTLĘ
# ===========================================================================
def przyklad_27_for_czy_while():
    """Dwie pętle wykonujące podobną pracę, ale sterowane inaczej."""
    # for dobrze pasuje do sytuacji, kiedy liczba powtórzeń jest znana
    # lub mamy konkretną sekwencję (np. znaki tekstu, zakres liczb).
    for i in range(3):  # Wiemy z góry: dokładnie trzy powtórzenia.
        print('for:', i)  # Kolejno pokażemy bieżące wartości i: 0, 1, 2.

    # while pasuje do sytuacji, gdy działamy DO SPEŁNIENIA / ZMIANY WARUNKU.
    # Tutaj dajemy licznik, aby przedstawić porównywalny, kończący się kod.
    count = 0  # Początek licznika pętli while.
    while count < 3:  # Warunek jest sprawdzany przed każdą iteracją.
        print('while:', count)  # Pokazujemy bieżącą wartość licznika.
        count += 1  # Zmieniamy licznik, żeby warunek w końcu był fałszywy.

    # Wskazówki z prezentacji:
    # - Dokładnie 10 powtórzeń? -> zwykle for.
    # - Każdy znak napisu? -> zwykle for.
    # - Liczby od 1 do N? -> zwykle for.
    # - Pytanie ponawiane aż do poprawnej odpowiedzi? -> zwykle while.
    # - Powtarzanie aż do zajścia losowego zdarzenia? -> zwykle while.
    # - Menu otwarte aż do wyboru „Wyjdź”? -> zwykle while.


if __name__ == '__main__':
    przyklad_27_for_czy_while()  # Uruchom tylko to jedno zadanie.
