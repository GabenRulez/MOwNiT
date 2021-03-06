# Algorytm Kahana

# Zaimplementuj algorytm sumowania Kahana.

# 1.    Wyznacz bezwzględny i względny błąd obliczeń dla tych samych danych wejściowych jak w przypadku testów z Zadania 1.

# 2.    Wyjaśnij dlaczego w algorytm Kahana ma znacznie lepsze własności numeryczne? Do czego służy zmienna err?

# 3.    Porównaj czasy działania algorytmu Kahana oraz algorytmu sumowania rekurencyjnego dla tych samych danych wejściowych.

import numpy as np
import textFunctions
from textFunctions import *
import time

### Funkcje pomocnicze z lab01/zad1.py ###

def tworzMacierzOJednakowychWartosciach(wartosc, wielkosc):
    macierz = np.full((wielkosc), wartosc, dtype=np.float32)
    return macierz

def bladBezwzgledny(wartosc_dokladna, wartosc_zmierzona):
    return abs(wartosc_dokladna - wartosc_zmierzona)

def bladWzgledny(wartosc_dokladna, wartosc_zmierzona):
    if wartosc_dokladna==0:
        wartosc_dokladna = 1e-16
    return ( bladBezwzgledny( wartosc_dokladna, wartosc_zmierzona ) ) / wartosc_dokladna

def losowaLiczbaZPrzedzialu(zakres_start, zakres_end):
    wartosc = (zakres_end - zakres_start) * np.random.random(1) + zakres_start
    return wartosc[0]

def sumaBinarna(tablica):
    start = 0
    koniec = len(tablica)-1
    return pomocSumyBinarnej(tablica, start, koniec)

def pomocSumyBinarnej(tablica, start, koniec):
    if start == koniec:
        return tablica[start]

    elif start + 1 == koniec:
        return tablica[start] + tablica[koniec]

    else:
        breakout = int( int(start+koniec)/2 )
        return pomocSumyBinarnej(tablica, start, breakout) + pomocSumyBinarnej(tablica, breakout+1, koniec)

### Koniec funkcji pomocniczych


def sumaKahana(tab):
    sum = np.float32(0.0)
    err = np.float32(0.0)

    for i in range(len(tab)):
        y = tab[i] - err
        # print("y    jest typu {}".format(type(y)))
        temp = sum + y
        # print("temp jest typu {}".format(type(temp)))
        err = (temp - sum) - y
        sum = temp
    return sum







printTitle("Początek programu")

wartosc = np.float32( losowaLiczbaZPrzedzialu(0.1, 0.9) )
N = 10000000    # N = 10^7
macierz = tworzMacierzOJednakowychWartosciach(wartosc, N)

print("Wartość wybranej losowej liczby to {}.".format(wartosc))
print("Wielkość macierzy to {}.".format(N))


printSpacer()


printTitle("Suma Kahana")
tempSuma = sumaKahana(macierz)
tempProsteMnozenie = wartosc * N
print("Obliczona suma: {}".format(tempSuma))
print("Wynik mnożenia: {}".format(tempProsteMnozenie))
printSpacer()
tempBladBezwzgledny = bladBezwzgledny(tempProsteMnozenie, tempSuma)
tempBladWzgledny = bladWzgledny(tempProsteMnozenie, tempSuma)
print("Błąd bezwzględny: {}".format(tempBladBezwzgledny))                           # 2.1
print("Błąd względny: {} = {}%".format(tempBladWzgledny, tempBladWzgledny*100))     # Błędy bezwzględny i względny

# 2.2
# Algorytm Kahana ma znacznie lepsze własności numeryczne szczególnie w porównaniu z "prostym sumowaniem",
# gdyż zmienna "err" przechowuje małostkowy błąd numeryczny
# (który powstaje przy "obcinaniu" cyfr znaczących małej liczby w operacji dodania do dużej liczby)
# i likwiduje go przy następnej operacji dodawania.

printSpacer(2)
printTitle("Porównanie czasu wykonania dla dwóch algorytmów",0)
printTitle("(tj. algorytmu Kahana i algorytmu sortowania rekurencyjnego", 0)
printSpacer()

N2 = 10000000
print("Tworzę nową macierz o {} elementach.".format(N2))
macierz2 = tworzMacierzOJednakowychWartosciach(wartosc, N2)
printSpacer()

start = time.process_time()
sumaKahana(macierz2)
czas_1 = time.process_time() - start

start = time.process_time()
sumaBinarna(macierz2)
czas_2 = time.process_time() - start

print("Czas 'sumy Kahana':   {}s".format(czas_1))
print("Czas sumy 'binarnej': {}s".format(czas_2))

# 2.3
# Czasy dla tych dwóch algorytmów są bardzo zbliżone do siebie.
# Przy kilkunastu testach wynika, że algorytm "sumy binarnej" jest nieco szybszy, około 3-5%