# testing weather algoritm

x = 40
licznik = {}

for i in range(157):
    number = ((i * 7) + 3 + (int(i//x) * 7)) % x  # Przykładowe złożone wyrażenie
    if number in licznik:
        licznik[number] += 1
    else:
        licznik[number] = 1

for number, ilosc in licznik.items():
    print(f"Liczba {number} pojawiła się {ilosc} razy.")