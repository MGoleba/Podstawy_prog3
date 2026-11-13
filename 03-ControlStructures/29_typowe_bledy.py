# -*- coding: utf-8 -*-
# Samodzielny przykład nr 29 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 29. COMMON BEGINNER MISTAKES — PIĘĆ CZĘSTYCH BŁĘDÓW
# ===========================================================================
def przyklad_29_typowe_bledy():
    """Pokazuje POPRAWNE warianty; błędne warianty są tylko komentarzami."""

    # BŁĄD 1: BRAKUJĄCY DWUKROPEK.
    # BŁĘDNIE: if x > 0
    # Po warunku if, elif, else, for lub while wpisujemy znak :.
    x = 5  # Przykładowa liczba używana w poprawnych wersjach.
    if x > 0:  # Dwukropek kończy nagłówek instrukcji if.
        print('Liczba dodatnia')  # Cztery spacje wskazują blok if.

    # BŁĄD 2: ZŁE WCIĘCIE.
    # BŁĘDNIE (bez wcięcia po if):
    # if x > 0:
    # print('Liczba dodatnia')
    # Wcięcie 4 spacji pozwala Pythonowi rozpoznać wnętrze if.
    if x > 0:  # Poprawnie otwieramy blok warunkowy.
        print('Poprawne wcięcie')  # Poprawnie umieszczamy linię wewnątrz bloku.

    # BŁĄD 3: UŻYWANIE = ZAMIAST ==.
    # BŁĘDNIE: if x = 5:
    # Znak = przypisuje wartość, a == sprawdza równość dwóch wartości.
    if x == 5:  # Sprawdzamy, czy x jest równe 5.
        print('x wynosi pięć')  # Kod wykona się, gdy porównanie zwróci True.

    # BŁĄD 4: PĘTLA NIESKOŃCZONA PRZEZ BRAK AKTUALIZACJI WARUNKU.
    # BŁĘDNIE:
    # count = 0
    # while count < 5:
    #     print(count)
    # Tutaj count nigdy nie rośnie, więc warunek zawsze jest True.
    count = 0  # Ustawiamy licznik początkowy.
    while count < 5:  # Powtarzamy, dopóki licznik jest mniejszy od 5.
        print(count)  # Wyświetlamy licznik.
        count += 1  # Zwiększamy licznik, żeby pętla mogła się zakończyć.

    # BŁĄD 5: MYLENIE KOŃCA RANGE.
    # range(1, 10) daje 1, 2, ..., 9; NIE zawiera liczby 10.
    # Jeśli chcemy wartości od 1 do 10 WŁĄCZNIE, podajemy range(1, 11).
    for number in range(1, 11):  # Uwzględniamy 1–10, pomijamy 11.
        print(number)  # Wyświetlamy każdą z dziesięciu liczb.

    # Wszystkie błędne fragmenty są zapisane jako komentarze, dlatego
    # nie psują działania pliku. Uruchamialny kod poniżej nich jest poprawny.


if __name__ == '__main__':
    przyklad_29_typowe_bledy()  # Uruchom tylko to jedno zadanie.
