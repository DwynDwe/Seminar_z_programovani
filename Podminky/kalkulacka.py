cislo1 = float(input('Zadejte první číslo: '))
cislo2 = float(input('Zadejte druhé číslo: '))
co = input('Zadejte operaci: ')
vysledek = None

if co == '+':
    vysledek = cislo1 + cislo2
elif co == '/' or co == ':':
    vysledek = cislo1 / cislo2
elif co == '*' or co == 'x':
    vysledek = cislo1 * cislo2
elif co == '-':
    vysledek = cislo1 - cislo2

print('Výsledek je: ', vysledek)