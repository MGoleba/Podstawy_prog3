# -*- coding: utf-8 -*-
# Samodzielny przykład nr 22 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 22. PRAKTYCZNE OPERACJE NA TEKŚCIE
# ---------------------------------------------------------------------------
def przyklad_22_metody_tekstu():
    """Długość napisu, wielkość liter, zliczanie i wyszukiwanie fragmentów."""
    movie = 'The Lord of the Rings: The Return of the King'  # Tytuł filmu.

    print(len(movie))      # len() liczy wszystkie znaki, również spacje i ':'.
    print(movie.upper())   # upper() tworzy napis z wielkimi literami.
    print(movie.lower())   # lower() tworzy napis z małymi literami.
    print(movie.count('e')) # count('e') liczy wystąpienia małej litery e.
    print(movie.find('Lord'))  # find() podaje indeks pierwszego znaku 'Lord'.

    # Kropka, np. movie.upper(), oznacza wywołanie metody na obiekcie movie.
    # upper() i lower() nie nadpisują same z siebie pierwotnej zmiennej.
    # Python rozróżnia małe i wielkie litery: 'e' jest inne niż 'E'.
    # find() zwróci -1, jeśli nie znajdzie szukanego fragmentu.


if __name__ == '__main__':
    przyklad_22_metody_tekstu()  # Uruchom tylko to jedno zadanie.
