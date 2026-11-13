# -*- coding: utf-8 -*-
# Samodzielny przykład nr 11 z pliku: struktury_sterujace
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ===========================================================================
# 11. LOGIN AND PASSWORD — SPRAWDZANIE LOGINU I HASŁA
# ===========================================================================
def przyklad_11_login_i_haslo():
    """Oba wpisane napisy muszą odpowiadać zapisanym wartościom."""
    login = 'joe'       # Wzorcowy login zapisany w przykładzie.
    password = 'abcd'   # Wzorcowe hasło w przykładzie dydaktycznym.

    entered_login = input('Login: ')        # Użytkownik wpisuje login (tekst).
    entered_password = input('Password: ')  # Użytkownik wpisuje hasło (tekst).

    # == porównuje napisy znak po znaku i uwzględnia wielkość liter.
    # and wymaga, aby i login, i hasło były poprawne JEDNOCZEŚNIE.
    if login == entered_login and password == entered_password:
        print('You are logged in')  # Wykonuje się tylko przy dwóch trafieniach.
    else:  # Gdy login jest zły, hasło jest złe lub oba są złe.
        print('Incorrect login or password')  # Nie zdradzamy, co dokładnie błędne.

    # TO NIE JEST BEZPIECZNY SYSTEM LOGOWANIA: hasło jest wprost w pliku,
    # a input() pokazuje wpisywane znaki. To tylko demonstracja operatora and.


if __name__ == '__main__':
    przyklad_11_login_i_haslo()  # Uruchom tylko to jedno zadanie.
