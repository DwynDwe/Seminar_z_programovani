# Byli jste pozadani mistni ZOO, abyste pro ne vytvorili primitivní informacni system, ktery bude obsahovat
# informace o zvířatech v ZOO.

# System bude umět přidat a odstranit zvire ze systemu,
# bude mozne zadat krmeni zvirete, zkontrolovat jeho zdravotni stav
# Informace v systemu jsou predstaveny ve forme pole, ktere obsahuje jednotliva zvirata (slovníky) a jejich stav (slovnik state), viz promenna animals
petshop = [
    {'species': 'hyena', 'name': 'Linda', 'sex': 'female', 'state': {'fed': True, 'healthy': True}, 'price': 100000},
    {'species': 'goldfish', 'name': 'Trudy', 'sex': 'female', 'state': {'fed': True, 'healthy': True}, 'price': 100},
    {'species': 'hippo', 'name': 'Limba', 'sex': 'female', 'state': {'fed': True, 'healthy': True}, 'price': 700000},
    {'species': 'lion', 'name': 'Vincent', 'sex': 'male', 'state': {'fed': True, 'healthy': True}, 'price': 400000},
]

money = 1000000

animals = [
    {'species': 'wolf', 'name': 'Boris', 'sex': 'male', 'state': {'fed': True, 'healthy': True}, 'price': 150000},
    {'species': 'wolf', 'name': 'Sable', 'sex': 'female', 'state': {'fed': False, 'healthy': True}, 'price': 100000},
    {'species': 'elephant', 'name': 'Suki', 'sex': 'female', 'state': {'fed': True, 'healthy': False}, 'price': 800000},
    {'species': 'eagle', 'name': 'Comet', 'sex': 'male', 'state': {'fed': False, 'healthy': False}, 'price': 70000},
    {'species': 'panda', 'name': 'Zelda', 'sex': 'female', 'state': {'fed': True, 'healthy': True}, 'price': 2500000},
]

# 2: nakrmeni zvirat: prochazejte polem a pokud nektere ze zvirat bude mit fed == False, tak vypiste do konzole,
# ze dane zvire bylo nakrmeno a nastavte hodnotu fed = True
def feed_animals():
    for i in animals:
        if i['state']['fed'] == False:
            print('Zvíře ' + i['species'] + ' ' + i['name'] + ' napapáno')
            i['state']['fed'] = True

# 3: vyleceni zvirat: obdobne jako u 2
def heal_animals():
    for i in animals:
        if i['state']['healthy'] == False:
            print('Zvíře ' + i['species'] + ' ' + i['name'] + ' vykurírováno')
            i['state']['health'] = True

# 4: nalezeni zvirat co maji hlad: prochazejte pole a pro kazde zvire zkontrolujte zda nema hlad. Pokud bude mit hlad,
# tak do konzole vypiste informace o zviratech co maji hlad vcetne celkoveho poctu zvirat co maji hlad (napr. Celkovy pocet hladovych zvirat: 2)
def find_hungry():
    hungry_animals = []
    for i in animals:
        if i['state']['fed'] == False:
            hungry_animals.append(i['species'] + ' ' + i['name'])
    print('Počrt hladových zvířat: ' + str(len(hungry_animals)))
    print('Která jsou hladová: ' + str(hungry_animals))

# 5: obdobne jako u 4, akorat pro klíč healthy
def find_ill():
    ill_animals = []
    for i in animals:
        if i['state']['healthy'] == False:
            ill_animals.append(i['species'] + ' ' + i['name'])
    print('Počet nemocných zvířat: ' + str(len(ill_animals)))
    print('Která jsou nemocná: ' + str(ill_animals))

# 6: Vypište nějak pěkne zformátovaný seznam všech zvířat v ZOO včetně informací o nich
# nevypisujte jen slovníky ve formě {'species': 'eagle'...} 
def print_animals():
    print('Seznam zvířat')
    for i in animals:
        print('Druh: ' + i['species'] + ', jméno: ' + i['name'] + ', pohlaví: ' + i['sex'] + ', hladový: ' + str(i['state']['fed']) + ', zdravý: ' + str(i['state']['healthy']) + ', cena: ' + str(i['price']))

# 7: Prodejte zvíře podle zadaného jména zvířete, peníze za prodej (price) přidejte do proměnné money
def sell_animal_by_name(name):
    global money
    for i in range(len(animals)):
        if animals[i]['name'] == name:
            money = money + animals[i]['price']
            del animals[i]
            break


# 8: Prodejte víc zvířat najednou. Na vstupu bude seznam jmen zvířat, které chcete prodat. Peníze za prodej přičtěte do proměnné money
def sell_animals_by_name(names):
    global money
    names_list = names.split(';')
    sold = []
    for sell_name in names_list:
        for i in animals:
            if i['name'] == sell_name:
                sold.append(i)
    for animal in sold:
        money = money + animal['price']
        animals.remove(animal)


# 9 Kupte z "Petshopu" zvíře podle druhu a přidejte ho do ZOO (proměnná animals). Odečtěte z pokladny peníze
# Pokud zvíře bude moc drahé tak vypište, že na příslušné zvíře nemáte peníze a funkci ukončete.
def buy_animal_by_specie(specie):
    global money
    for new_animal in petshop:
        if new_animal['species'] == specie and new_animal['price'] <= money:
            animals.append(new_animal)
            money = money - new_animal['price']
            return print('Zvíře zakoupeno')
    return print('Nemáte dost peňázků')



NAME_OF_THE_ZOO = 'Tvoje Máma'
print('Vítejte v informačním systému ZOO {}'.format(NAME_OF_THE_ZOO))

while True:
    answer = int(input('Vyberte jednu z možností:\n'
                       '1: Koupit nové zvíře\n'
                       '2: Nakrmit zvířata\n'
                       '3: Výlečit zvířata\n'
                       '4: Najít zvířata co mají hlad\n'     
                       '5: Najít zvířata co jsou nemocná\n'   
                       '6: Vypsat všechna zvířata\n'
                       '7: Prodat zvíře podle názvu\n'
                       '8: Prodat více zvířat podle názvu\n'
                       '9: Ukončit systém\n'))

    if answer == 1:
        specie = input('Zadejte druh: \n')
        buy_animal_by_specie(specie)
    elif answer == 2:
        feed_animals()
    elif answer == 3:
        heal_animals()
    elif answer == 4:
        find_hungry()
    elif answer == 5:
        find_ill()
    elif answer == 6:
        print_animals()
    elif answer == 7:
        name = input('Zadejte název: \n')
        sell_animal_by_name(name)
    elif answer == 8:
        # vymyslete nebo najděte pomocí které funkce vytvoříte z řetězce odděleného středníky seznam, který pošlete do funkce
        name = input('Zadejte název více zvířat (názvy oddělte středníkem): \n')
        sell_animals_by_name(name)
    elif answer == 9:
        print('Ukončování programu...')
        break
