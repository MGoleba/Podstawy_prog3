# -*- coding: utf-8 -*-
# Samodzielny przykład nr 30 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 30. COMMON BEGINNER MISTAKES — BŁĘDY POCZĄTKUJĄCYCH
# ---------------------------------------------------------------------------
def przyklad_30_typowe_bledy():
    """Pięć typowych błędów i ich bezpieczne, poprawne odpowiedniki."""
    # BŁĄD NR 1: BRAK ZAMIANY WARTOŚCI Z INPUT() NA LICZBĘ.
    # NIEPOPRAWNIE: result = input('Podaj liczbę: ') + 5
    # Dlaczego? input() zwraca str, a nie da się dodać int do str przez +.
    number = int('10')  # int zamienia napis '10' w liczbę 10.
    result = number + 5 # Dodajemy dwie liczby, więc działanie jest poprawne.
    print(result)       # Pokazujemy wynik prawidłowego dodawania.

    # BŁĄD NR 2: LITERÓWKA W NAZWIE ZMIENNEJ.
    # NIEPOPRAWNIE: average = 10; print(averege)
    # „average” i „averege” to dla Pythona DWIE RÓŻNE NAZWY.
    average = 10       # Tworzymy zmienną o konkretnej nazwie.
    print(average)     # Odwołujemy się do dokładnie tej samej nazwy.

    # BŁĄD NR 3: MYLENIE = Z ==.
    # = przypisuje wartość, a == sprawdza równość wartości.
    x = 5              # Przypisujemy do x wartość 5.
    print(x == 5)      # Porównujemy x z 5, otrzymując bool.

    # BŁĄD NR 4: NIEPOPRAWNA KOLEJNOŚĆ DZIAŁAŃ.
    a = 10             # Pierwsza liczba do obliczenia średniej.
    b = 20             # Druga liczba do obliczenia średniej.
    # NIEPOPRAWNIE: average = a + b / 2 (dzielenie ma pierwszeństwo).
    average = (a + b) / 2  # Najpierw suma, potem dzielenie przez dwa.
    print(average)     # Pokazujemy średnią arytmetyczną.

    # BŁĄD NR 5: NIEZAMKNIĘTY CUDZYSŁÓW LUB APOSTROF.
    # NIEPOPRAWNIE: name = 'Adam
    # Prawa strona musi mieć cudzysłów/apostrof zamykający napis.
    name = 'Adam'      # Poprawnie zapisany tekst (typ str).
    print(name)        # Pokazujemy tekst.


if __name__ == '__main__':
    przyklad_30_typowe_bledy()  # Uruchom tylko to jedno zadanie.
