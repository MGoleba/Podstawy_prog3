# -*- coding: utf-8 -*-
# Samodzielny przykład nr 08 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 8. KOLEJNOŚĆ WYKONYWANIA DZIAŁAŃ
# ---------------------------------------------------------------------------
def przyklad_08_kolejnosc_dzialan():
    """Nawiasy, potęgi, mnożenie, dzielenie, dodawanie i porównania."""
    # W działaniu poniżej kolejność jest następująca:
    # (1) potęga 2 ** 2; (2) dzielenie 4 / 4; (3) dodawanie 4 + 1.0.
    print(4 + 4 / 2 ** 2)

    # % ma pierwszeństwo przed +. Najpierw obliczymy 4 % 4, potem + 4.
    print(4 + 4 % 4)

    # Python oblicza sumy po obu stronach znaku <, a następnie je porównuje.
    # Najpierw: 4 + 1 i 2 + 2. Na końcu sprawdzamy: czy 5 < 4?
    print(4 + 1 < 2 + 2)

    # Nawiasy służą również do wymuszenia wybranej kolejności obliczeń.
    print((4 + 4) / 2)  # Najpierw 4 + 4, potem dzielenie przez 2.


if __name__ == '__main__':
    przyklad_08_kolejnosc_dzialan()  # Uruchom tylko to jedno zadanie.
