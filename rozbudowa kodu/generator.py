ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
loty = ((a,b) for a in ports for b in ports if a != b if a < b)
liczba = 0
for (a,b) in loty:
    print(a, " - ", b)
    liczba += 1
print(liczba)