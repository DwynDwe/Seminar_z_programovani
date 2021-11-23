age = 15

# podmínky větví program. Každá část podmínky (kromě else) má svůj výraz, který se vyhodnocuje buď jako True nebo False
# Pokud se vyhodnotí jako True, tak se vykoná blok kódu pod podmínkou.
# Blok kódu začíná za : a je odsazený o 4 mezery (nebo 1 tabulátor). Může obsahovat i více příkazů.
if age < 17:
    print('ses teenager')
elif age < 25:
    print('ses mladsi')
else:
    print('ses starsi')

# import knihovny, která je obsažena v Pythonu (není to knihovna 3. strany)
import random
# funkce z knihovny se pak volá přes název knihovny a tečku
print(random.randint(0, 2))

# z knihovny můžete naimportovat jen konkrétní funkci
from random import randint
print(randint(0, 2))

# importované funkci nebo knihovně můžete také přiřadit alias
from random import randint as random_number
print(random_number(0, 2))


from random import randint
state = randint(0, 3)

if state == 0:
    print('Auto stoji')
elif state == 1:
    print('Auto se rozjíždí')
elif state == 2:
    print('Auto jede')
else:
    print('Semafor nejede auta dávají přednost')


# list (seznam, pole, array). Hranaté závorky
# hranatou závorku napíšete na české klávesnici: ALT GR + F nebo G
# můžete taky použít anglickou klávesnici
l = [1, 2, 3, 4, 5]
print(l)

# v listu se dá kombinovat spousta datových typů, včetně dalšího listu
l2 = [1, 'ahoj', 10, 1000.5, [0, 1], True]


names = ['Honza', 'Martin', 'Hana']
print(names) 
# nový prvek na konec pole přidáme pomocí funkce append()
names.append('Jirka')
print(names)
# přistupovat lze pomocí indexů
print(names[0], names[3])

# tuple se vytváří pomocí složených závorek a je neměnný
names = ('Honza', 'Martin', 'Hana')
print(names[0])
names[0] = 'jiné jmeno'

# set se vytváří pomocí složených závorek. Na české klávesnici je napíšete pomocí ALT GR + B nebo N
# set neobsahuje nikdy duplicity, ty se automaticky odstraní
# Také je množina neuspořádáná a tím pádem nejde použít indexy
names_set = {'Honza', 'Martin', 'Hana', 'Honza'}

# pokud chcete odstranit duplicity, tak můžete list přetypovat na set a pak zpátky na list
names = ['Honza', 'Martin', 'Hana', 'Honza']
print(list(set(names)))

# přidání do setu
names_set.add('Martin')
print(names_set)

# slovník je napsán pomocí složených závorek, ale hlavně obsahuje strukturu klíč:hodnota
# slovník může obsahovat jakýkoliv typ jako value, např. další slovník
person = {'name': 'Honza', 'age': 20, 'city': 'Zlín'}
person2 = {
    'name': 'Honza',
    'age': 20,
    'address': {
        'city': 'Zlín',
        'zip code': 76005
    }
}

# když chcete vybírat ze slovníku, tak pomocí hranatých závorek a klíče (pak se vám vrátí hodnota).
# Pokud přistupujete do slovníku uvnitř slovníku, tak můžete použít dva klíče (každý v hranaté závorce)
print(person2['age'], person2['address']['city'])

# Můžete také udělat dvojrozměrné pole. Jedno pole v sobě obsahuje další pole jako řádky.
map = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
]

print(map[1][1])
