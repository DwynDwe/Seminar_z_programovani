# napiste kod, ktery vezme dve vstupni hodnoty od uzivatele pomoci funkce input()
# tyto dve hodnoty prevede na integer a pote vydeli a vypise vysledek
# pokud uzivatel napriklad nazada cislo ale retezec nebo zada jako druhe cislo 0, tak vypisete chybu
# pouzijte try/except (ZeroDivisionError a ValueError)

value1 = input('Enter first number: ')
value2 = input('Enter second number: ')
division = None

try:
    division = int(value1)/int(value2)
except ZeroDivisionError:
    print('dělení nulou!')
except ValueError:
    print('Špatná hodnota!')

print(division)