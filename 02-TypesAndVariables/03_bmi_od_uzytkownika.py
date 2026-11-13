# -*- coding: utf-8 -*-
# Samodzielny przykład nr 03 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 3. SCRIPT MODE — BMI NA PODSTAWIE DANYCH WPISYWANYCH PRZEZ UŻYTKOWNIKA
# ---------------------------------------------------------------------------
def przyklad_03_bmi_od_uzytkownika():
    """Pobieranie wzrostu i masy, konwersja na liczby, obliczenie BMI."""
    # input() pokazuje pytanie i czeka na odpowiedź zakończoną klawiszem Enter.
    # WAŻNE: input() ZAWSZE zwraca tekst (typ str), nawet gdy wpiszemy cyfry.
    height = input('Enter your height in cm: ')  # Pobieramy wzrost jako tekst.
    weight = input('Enter your weight in kg: ')   # Pobieramy masę jako tekst.

    # int(tekst) próbuje zamienić tekst na liczbę całkowitą, np. '180' na 180.
    # Ponownie przypisujemy wartości do tych samych nazw zmiennych.
    height = int(height)  # Wzrost może teraz brać udział w obliczeniach.
    weight = int(weight)  # To samo robimy z masą ciała.

    # W Pythonie ** 2 oznacza „do kwadratu”; / oznacza zwykłe dzielenie.
    # Najpierw przeliczamy cm na m, następnie podnosimy wzrost do kwadratu.
    bmi = weight / (height / 100) ** 2  # Wzór: masa_kg / (wzrost_m ** 2).

    # print() może otrzymać tekst oraz wynik oddzielone przecinkiem.
    # round(bmi, 2) pozwala uniknąć wyświetlania wielu cyfr po kropce.
    print('Your BMI is', round(bmi, 2))

    # Uwaga: int() nie przyjmuje tekstu '77.5'. Dla wartości niecałkowitych
    # można użyć float() — zostanie to pokazane w kolejnych przykładach.
    # Wzrost musi być większy od 0, bo nie wolno dzielić przez zero.


if __name__ == '__main__':
    przyklad_03_bmi_od_uzytkownika()  # Uruchom tylko to jedno zadanie.
