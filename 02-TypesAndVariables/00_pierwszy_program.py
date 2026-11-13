# -*- coding: utf-8 -*-
# Samodzielny przykład nr 00 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 0. PIERWSZY PROGRAM — WYŚWIETLANIE TEKSTU
# ---------------------------------------------------------------------------
def przyklad_00_pierwszy_program():
    """Poznajemy polecenie print() i tekst typu str."""
    # print() to wbudowana funkcja, która pokazuje wynik w terminalu.
    # Tekst umieszczamy między cudzysłowami; bez nich Python szukałby zmiennej.
    # Nawiasy () otaczają argumenty, czyli informacje przekazane do funkcji.
    print("Cześć, świecie!")  # Wyświetlamy dokładnie podany napis.


if __name__ == '__main__':
    przyklad_00_pierwszy_program()  # Uruchom tylko to jedno zadanie.
