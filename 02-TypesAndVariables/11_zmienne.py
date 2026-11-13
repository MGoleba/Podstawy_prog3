# -*- coding: utf-8 -*-
# Samodzielny przykład nr 11 z pliku: podstawy_pythona
# Uruchom: python NAZWA_PLIKU.py (lub py NAZWA_PLIKU.py w Windows).

# ---------------------------------------------------------------------------
# 11. VARIABLE — ZMIENNE
# ---------------------------------------------------------------------------
def przyklad_11_zmienne():
    """Zapisujemy informacje o firmie i obliczamy kwotę na pracownika."""
    company = 'ABC Data'      # company: nazwa firmy (tekst typu str).
    employees = 25            # employees: liczba pracowników (int).
    remote_work = True        # remote_work: dostępność pracy zdalnej (bool).

    # / dzieli podaną liczbę przez wartość zmiennej employees.
    # Wynik dzielenia jest zapisany w nowej zmiennej income_per_person.
    income_per_person = 4500000 / employees

    print(company)            # Odczytujemy i wyświetlamy nazwę firmy.
    print(employees)          # Odczytujemy liczbę pracowników.
    print(remote_work)        # Pokazujemy wartość logiczną.
    print(income_per_person)  # Pokazujemy kwotę przypadającą na pracownika.

    # Uwaga: „kwota na pracownika” to tutaj wyłącznie wynik matematyczny,
    # a nie rzeczywista informacja o wynagrodzeniu pracowników firmy.


if __name__ == '__main__':
    przyklad_11_zmienne()  # Uruchom tylko to jedno zadanie.
