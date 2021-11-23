# názvy proměnných bez diakritiky, mezery nahradit _, malé písmena
my_name = 'Petr Šilhák'
name = 'PETR'

print(name)
lower = name.lower()
print(lower)

# předchozí kód je možné napsat i na jeden řádek. Funkce se vykonají od prostředku. Nejdříve name.lower() a výsledek této funkce se pošle do print()
print(name.lower())

num = 1  # int
num = 1.5  # float

print(num)

# typ boolean může nabývat hodnot True nebo False. Použít lze taky 1 a 0
x = True
print(type(x))
x = 1
print(type(x)) 

y = False
y = 0

# Proměnná taky nemusí mít žádnou hodnotu. Pak se používá klíčové slovo None (podobně jako NULL v databázi)
c = None

# proměnnou můžu "vytvořit" i znovu (přepsat hodnotu)
name = 'PETR'
x = 1
y = False

# funkce type(obj) vrací typ proměnné
print(type(name))
print(type(x))
print(type(y))

# '10' je řetězec, ale lze přetypovat na číslo pomocí funkce int(obj)
# stejně tak můžete použít i přetypování dalších typů bool(obj), float(obj), str(obj)
num = '10'
print(type(num))
num = int(num)
print(type(num))

print(bool(10))

# můžete použít operátory. Přednost je určena klasicky matematickými pravidly. Pokud ji chcete ovlivnit tak použijete závorky
print((1 + 1) + (10 / num))
print(2 * 'ahoj')
print(num * 1)

# výrazy mají své operátory. Tady je vidět porovnání ==, negace porovnání (nerovná se) !=, a větší nebo rovno (>=) 
print(1 == 1)
print(num != 1)
print(num >= 1)

# funkce input program zastaví a čeká na vstup od uživatele. Výstupem funkce je řetězec. V tomto případě se řetězec zapíše do proměnnýc c1 a c2
# protože chceme ale číslo, tak rovnou číslo přetypujeme na int funkcí
c1 = int(input('Zadejte číslo 1:'))
c2 = int(input('Zadejte číslo 2:'))

print(c1 + c2)