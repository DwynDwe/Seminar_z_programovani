# v tomto ukolu budete simulovat lednici vcetne jejiho obsahu
# lednici bude predstavovat nejdrive prazdne pole (promenna fridge)
fridge = []

# jednotlive potraviny budou reprezentovany slovnikem napr.
# name: predstavuje nazev potraviny
# price: predstavuje cenu
# expired: popisuje jestli je potravina prosla nebo ne
# cheese = {'name': 'blue cheese', 'price': 40, 'expired': True}


def add_food(food):
    if food['expired'] == True:
        return False
    else:
        fridge.append(food)
        return True
    """
    Funkce, ktera prida do lednice potravinu (pouze kdyz neni prosla).
    Pri uspesnem naplneni vrati True, pri neuspesnem False.
    :param (dict) food: potravina, kterou budete vkladat
    :return (bool): vraci True, kdyz potravina byla pridana do lednice. Jinak vraci False
    """

def add_foods(*args):
    any_expired = False
    for item in args:
        if item['expired'] == True:
            any_expired = True
        else:
            fridge.append(item)
    if any_expired == True:
        return False
    else:
        return True

    """
    Funkce prida do lednice vice potravin (pouze kdyz nejsou prosle), ktere budou zadany jako jednotlive parametry funkce
    :param (dicts) args: vice potravin zadanych jako jednotlive parametry
    :return: vrati True pokud se vsechny potraviny podari pridat. Pokud ne, tak vrati False
    """
    pass

def eat_food(name):
    eat_item = False
    for dictionary in fridge:
        if fridge[dictionary]['name'] == name:
            del fridge[dictionary]
            eat_item = True
            break
    if eat_item == True:
        return True
    else:
        return False
    """
    Funkce, ktera odstrani z lednice potravinu pokud v ni potravina byla
    :param (str) name: nazev potraviny, kterou budete odebirat
    :return (bool): vraci True, kdyz potravina byla odebrana z lednice. Jinak vraci False
    """

def get_price():
    sum = 0
    for dictionary in range(len(fridge)):
        sum = sum + int(fridge[dictionary]['price'])
    return sum
    """
    Funkce, ktera vrati sumu cen vsech potravin v lednici
    :return (int): suma cen vsech potravin v lednici
    """
    pass

def get_count():
    return len(fridge)
    """
    Funkce vrati pocet vsech potravin v lednici
    :return (int): pocet vsech potravin v lednici. Stejne potraviny nemuzou byt v lednici vickrat
    """

def get_average_price():
    return get_price()/get_count() 
    """
    Funkce vrati prumernou cenu vsech potravin v lednici. Pouzijte funkce get_price() a get_count().
    :return (float): vrati prumernou cenu vsech potravin v lednici
    """

def remove_expired():
    expired_food = []
    counter = 0
    while counter != len(fridge):
        counter = 0
        for dictionary in range(len(fridge)):
            if fridge[dictionary]['expired'] == True:
                expired_food.append(fridge[dictionary])
                fridge[dictionary] = {}
                del fridge[dictionary]
                break
            else:
                counter += 1
    return expired_food
    """
    Funkce odstrani z lednice vsechny potraviny, ktere jsou prosle. Prosle potraviny funkce vrati. Pokud funkce
    zadne potraviny neodstrani tak funkce vrati prazdny seznam
    :return (list): seznam s proslymi potravinami
    """

def set_expired(name):
    for dictionary in range(len(fridge)):
        if fridge[dictionary]['name'] == name:
            fridge[dictionary]['expired'] = True
            return True
    return False
    """
    Funkce nastavi parametr potraviny expired na True podle jmena potraviny
    :param (str) name: nazev potraviny, ktere nastavi expired na True
    :return (bool): pokud funkce najde potravinu a nastavi ji hodnotu na True nebo jiz True mit bude vraci True.
                    pokud funkce nenajde podle nazvu zadanou potravinu, tak vrati False
    """


# Pokud budete chtit testovat jednotlive funkce muzete si je zavolat sami nebo muzete vyuzit volani zakomentovanych funkci nize
# Volani funkci nize neupravujte. Nakonci je odkomentujte (vymazte ''' '''). Podle vypisu poznate spravnost implementace.


# SPRAVNY VYPIS BY MEL VYPADAT TAKTO
# Pridani potraviny blue cheese: False
# Pridani potraviny milk: True
# Pridani vice potravin: True
# Snedl jsem sunku: True
# Snedl jsem hovinko: False
# Celkova cena potravin: 304
# Celkovy pocet potravin: 5
# Prumerna cena potravin: 60.8
# Nastavuji expiraci vajicku: True
# Nastavuji expiraci vinu: True
# Nastavuji expiraci hovinku: False
# Odstranene potraviny: [{'name': 'egg', 'price': 4, 'expired': True}, {'name': 'wine', 'price': 200, 'expired': True}]


print('Pridani potraviny blue cheese:', add_food({'name': 'blue cheese', 'price': 40, 'expired': True}))
print('Pridani potraviny milk:', add_food({'name': 'milk', 'price': 15, 'expired': False}))

print('Pridani vice potravin:', add_foods({'name': 'ham', 'price': 30, 'expired': False},
                                           {'name': 'salad', 'price': 45, 'expired': False},
                                           {'name': 'egg', 'price': 4, 'expired': False},
                                           {'name': 'wine', 'price': 200, 'expired': False},
                                           {'name': 'orange juice', 'price': 40, 'expired': False}))

print('Snedl jsem sunku:', eat_food('ham'))
print('Snedl jsem hovinko:', eat_food('poop'))

print('Celkova cena potravin:', get_price())

print('Celkovy pocet potravin:', get_count())

print('Prumerna cena potravin:', get_average_price())

print('Nastavuji expiraci vajicku:', set_expired('egg'))
print('Nastavuji expiraci vinu:', set_expired('wine'))
print('Nastavuji expiraci hovinku:', set_expired('poop'))

print('Odstranene potraviny:', remove_expired())