# Sumowanie liczb pojedynczej precyzji

# 1.    Napisz program, który oblicza sumę N liczb pojedynczej precyzji przechowywanych w tablicy
#       o N = 10^7  elementach. Tablica wypełniona jest tą samą wartością v z przedziału [0.1, 0.9] np. v = 0.53125.

# 2.    Wyznacz bezwzględny i względny błąd obliczeń. Dlaczego błąd względny jest tak duży?

# 3.    W jaki sposób rośnie błąd względny w trakcie sumowania?
#       Przedstaw wykres (raportuj wartość błędu co 25000 kroków) i dokonaj jego interpretacji.

# 4.    Zaimplementuj rekurencyjny algorytm sumowania, działający jak na rysunku poniżej.
#       (niczym drzewo binarne)

# 5.    Wyznacz bezwzględny i względny błąd obliczeń. Dlaczego błąd względny znacznie zmalał?

# 6.    Porównaj czas działania obu algorytmów dla tych samych danych wejściowych.

# 7.    Przedstaw przykładowe dane wejściowe, dla których algorytm sumowania rekurencyjnego zwraca niezerowy błąd.


import numpy as np
import textFunctions
from textFunctions import *


def prostaSuma(tablica):
    wynik = 0
    for i in range(len(tablica)):
        wynik+=tablica[i]
    return wynik

def tworzLosowaMacierz(zakres_start, zakres_end, wielkosc):
    macierz = (zakres_end - zakres_start) * np.random.random_sample(wielkosc) + zakres_start
    return macierz

def tworzMacierzOJednakowychWartosciach(wartosc, wielkosc):
    macierz = np.full((wielkosc), wartosc)
    return macierz

def losowaLiczbaZPrzedzialu(zakres_start, zakres_end):
    wartosc = (zakres_end - zakres_start) * np.random.random(1) + zakres_start
    return wartosc[0]

def bladBezwzgledny(wartosc_dokladna, wartosc_zmierzona):
    return abs(wartosc_dokladna - wartosc_zmierzona)

def bladWzgledny(wartosc_dokladna, wartosc_zmierzona):
    return ( bladBezwzgledny( wartosc_dokladna, wartosc_zmierzona ) ) / wartosc_dokladna

###########################################################

printTitle("Początek programu")

wartosc = losowaLiczbaZPrzedzialu(0.1, 0.9)
N = 10000000    # N = 10^7
macierz = tworzMacierzOJednakowychWartosciach(wartosc, N)

print("Wartość wybranej losowej liczby to {}.".format(wartosc))
print("Wielkość macierzy to {}.".format(N))


printSpacer()


printTitle("'Prosta suma' - najzwyklejsze dodawanie")
tempProstaSuma = prostaSuma(macierz)
tempProsteMnozenie = wartosc * N
print("Obliczona suma: {}".format(tempProstaSuma))
print("Wynik mnożenia: {}".format(tempProsteMnozenie))
printSpacer()
print("Błąd bezwzględny: {}".format(bladBezwzgledny(tempProsteMnozenie, tempProstaSuma)))
print("Błąd względny: {}".format(bladWzgledny(tempProsteMnozenie, tempProstaSuma)))

