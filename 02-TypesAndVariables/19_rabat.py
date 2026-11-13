# -*- coding: utf-8 -*-
# Samodzielny przykład nr 19 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 19. PROGRAM OBLICZENIOWY — CENA PO RABACIE
# ---------------------------------------------------------------------------
def przyklad_19_rabat():
    """Pobieramy cenę i rabat, obliczamy cenę końcową oraz oszczędność."""
    # input() pobiera tekst, a float() zamienia go na liczbę dziesiętną.
    # Najpierw wykonuje się funkcja WEWNĘTRZNA input(), później float().
    price = float(input('Enter price: '))
    discount = float(input('Enter discount %: '))

    # discount / 100 zamienia procent na ułamek, np. 15% na 0.15.
    # 1 - discount / 100 oznacza część pierwotnej ceny, którą trzeba zapłacić.
    # Przykładowo po rabacie 15% pozostaje do zapłaty 85% ceny.
    new_price = price * (1 - discount / 100)

    # Różnica ceny początkowej i nowej to zaoszczędzona kwota.
    reduction = price - new_price

    # f-string umożliwia wstawienie wartości new_price i reduction do zdania.
    # Zapis :.2f wymusza dokładnie dwa miejsca po kropce, np. 170.00.
    print(f'Price with discount: {new_price:.2f}')
    print(f'Reduction: {reduction:.2f}')

    # Ten prosty przykład zakłada sensowne dane wejściowe (np. rabat 0–100%).


if __name__ == '__main__':
    przyklad_19_rabat()  # Uruchom tylko to jedno zadanie.
