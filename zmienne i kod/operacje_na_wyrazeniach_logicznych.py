import os

def nie_wiem_co_pisze(a):
    with open(a, 'r') as f:
        tresc = f.read()
        ilosc_slow = len(tresc.split())
    return ilosc_slow

a = r't:\test\bulbul.txt'
if os.path.isfile(a):
    print("W pliku {} jest {} słów".format(a, nie_wiem_co_pisze(a)))
