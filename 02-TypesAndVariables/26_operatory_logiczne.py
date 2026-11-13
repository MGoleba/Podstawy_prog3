# -*- coding: utf-8 -*-
# Samodzielny przykład nr 26 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 26. LOGICAL OPERATORS — AND, OR I NOT
# ---------------------------------------------------------------------------
def przyklad_26_operatory_logiczne():
    """Łączymy i odwracamy warunki logiczne."""
    speed = 120  # Zapisujemy przykładową prędkość samochodu.

    # and oznacza „ORAZ”: oba warunki muszą być prawdziwe.
    # Sprawdzamy, czy prędkość mieści się w przedziale 40–140 włącznie.
    speed_ok = speed >= 40 and speed <= 140
    print(speed_ok)  # Wyświetlamy wynik obu warunków naraz.

    car_number = 'KR12345'  # Numer rejestracyjny jest tekstem (str).

    # [0:2] wybiera dokładnie dwa pierwsze znaki, czyli np. 'KR'.
    # == sprawdza równość tekstów; or oznacza „LUB”.
    # Wystarczy, że chociaż jeden z warunków połączonych przez or jest True.
    is_krakow = car_number[0:2] == 'KR' or car_number[0:2] == 'KK'
    print(is_krakow)  # Wyświetlamy wynik sprawdzenia prefiksu.

    # not odwraca wartość logiczną: True zmienia na False i odwrotnie.
    print(not speed_ok)  # Pokazujemy zaprzeczenie wcześniejszego sprawdzenia.

    # and: True tylko wtedy, gdy oba warunki są prawdziwe.
    # or: True wtedy, gdy co najmniej jeden warunek jest prawdziwy.
    # not: zamienia True na False, a False na True.


if __name__ == '__main__':
    przyklad_26_operatory_logiczne()  # Uruchom tylko to jedno zadanie.
