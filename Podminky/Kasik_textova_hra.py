from colorama import Fore as color
import time
import random

stats = {
    'health' : 5,
    'sanity' : 5,
    'money' : 100
}

world_parties = ['sever','s','jih','j','západ','z','zapad','východ','v','vychod']
yes_no = ['ano','ne','a','n']
end_station = ['podchod','p','konečná','k','konecna']

def print_stats():
    print('zdraví: ' + str(stats['health']) + '\npříčetnost: ' + str(stats['sanity']) + '\npeníze: ' + str(stats['money']))

def start():
    decision = input(color.YELLOW + 'Vítej v Brně! Ve městě, kde je možné všechno. A že je to fakt drsný místo, dokládají i novinové titulky:\n' + color.BLUE + '25. července 2021:' + color.RESET + ' Muž v parku v Brně tvrdil, že je král a máchal okolo sebe šroubovákem\n' + color.BLUE + '27. června 2021: ' + color.RESET +'Muž v prodejně v Brně přelepil mixér a reproduktor cenovkami zeleniny\n' + color.BLUE + '18. března 2018: ' + color.RESET + 'Přijel z Chebu na návštěvu do Brna, útočník mu ukousl nos\n' + color.YELLOW + 'Ještě je čas utéct. Chceš určitě zůstat? (ano/ne): ' + color.RESET).lower()
    print('\n')
    if decision == 'ano' or decision == 'a':
        print(color.YELLOW + 'Výborně! Vydejme se na dobrodružství! Toto jsou tvoje statistiky:\n' + color.RESET + 'zdraví: ' + str(stats['health']) + '\npříčetnost: ' + str(stats['sanity']) + '\npeníze: ' + str(stats['money']))
        print(color.YELLOW + 'Tyto statistiky jsou důležité pro tvé přežití. Nikdy se nesmí dostat na nulu. Nechceš přece, aby do tebe vrtal nějakej brněnskej felčar pazourkem. Každý úkol, který před tebou bude stát, ti při špatném vyřešení může ubrat některý z atributů. Tvé statistiky se objeví vždy, když dostaneš nějaké poškození (nebo za něco zaplatíš). Pokud se budeš muset rozhodnout, lze odpovědět jedním z textů v závorce. Lze použít i jen počáteční písmeno odpovědi. A teď vzhůru do Brna!\n' + color.RESET)
        train_station()
    else:
        print(color.YELLOW + 'Srabe. Támhle ti jede écéčko do Prahy.' + color.RESET)

def train_station():
    print(color.YELLOW + 'Jedna z nejhezčích brněnských budov. Společně s břeclavským nádrem nejstarší v zemi. Ale koho zajímá Břeclav. Navíc - máme tu bezdomovce a ti prostě patří k našemu koloritu. Hele, jeden přichází!' + color.RESET)
    print(color.BLUE + 'Bezdomovec:' + color.RESET + ' Čááu. Nemáš prosimtě ňáky bakule?')
    decision = input(color.YELLOW + 'Moc nechápeš, co po tobě chce, co? Hele, natahuje ruku! To bude chtít asi prachy! Dáš mu dvacku? (ano/ne): ' + color.RESET).lower()
    if decision == 'ano' or decision == 'a':
        print(color.BLUE + 'Bezdomovec: ' + color.RESET + 'Díky šéfe! Máte dobrý srdéčko\n\n' + color.YELLOW + 'Tak to proběhlo celkem hladce. Honem před budovu. Vypadá to, že se k tobě ženou další!\n'+ color.RESET)
        stats['money'] = stats['money'] - 20
        print_stats()
        near_train_station()
    else:
        print(color.BLUE + 'Bezdomovec: ' + color.RESET + 'Bleehhh\n\n' + color.YELLOW + 'Hehe. To jsi asi nečekal. Být hned po výstupu nahozenej bezdomovcem. To chceš. Běž radši rychle ven, než se stane něco dalšího.' + color.RESET)
        stats['sanity'] = stats['sanity'] - 2
        print_stats()
        near_train_station()

def near_train_station():
    while True:
        decision = input(color.YELLOW + 'Rušný místo. Spousta lidí se hrne přes sebe, ženou se na šaliny a trajfy. Co? Jo - trolejbusy. Bože.\nHlavas je prostě šíleně důležitý místo v Brně. Přes den se tu všechno děje a v noci, v noci vlastně taky. Tak kam teď? (sever, jih, západ, východ): ' + color.YELLOW).lower()
        if decision in world_parties:
            break
    if decision == 'sever' or decision == 's':
        print(color.YELLOW + 'Takže k šalině. Rovnou na věc. Pojeďme z toho drsnýho hlaváku přímo do štatlu - tam přežiješ dýl jak deset minut.' + color.RESET)
        time.sleep(3)
        tram_to_centre()
    elif decision == 'jih' or decision == 'j':
        print(color.YELLOW + 'Vracet se na nádr? Jsi vyměkl, srabe? Teď už necouvneš. Hybaj na šalinu!' + color.RESET)
        time.sleep(3)
        tram_to_centre()
    elif decision == 'západ' or decision == 'z' or decision == 'zapad':
        while True:
            decision = input(color.YELLOW + 'Nový sady jsou zajímavá ulice. Takový rovný nic. Mezi hlavákem a zástávkou pod Petrovem fakt nic není. Nechceš jít alespoň na ten Petrov? (ano/ne): ' + color.RESET).lower()
            if decision in yes_no:
                break
        if decision == 'ano' or decision == 'a':
            petrov()
        else:
            print(color.YELLOW + 'Ach jo. Si fakt nudnej...' + color.RESET)
            time.sleep(3)
            print(color.YELLOW + 'Hele, jede dvanáctka. Nastup.' + color.RESET)
            time.sleep (2)
            print('Nuda. Nic nebezpečného. Psychika? Lepší.')
            stats['sanity'] += 2
            tram_to_faculty()
    elif decision == 'východ' or decision == 'v' or decision == 'vychod':
        while True:
            decision = input(color.YELLOW + 'Nějaká konečná trolejbusu. A podchod. Kam teď? (podchod/konečná): ' + color.RESET).lower()
            if decision in end_station:
                break
        if decision == 'podchod' or decision == 'p':
            decision = None
            print(color.YELLOW + 'Temný místo. Patrioti tomu říkaj Myší díra. Vede většinou na nástupiště emhádéčka. Občas se tam někdo ztratí... Tak jdem.' + color.RESET)
            time.sleep(5)
            while True:
                decision = input(color.YELLOW + 'Hele, skořápky! Pojď, zahrajem si! (ano/ne): ' + color.RESET).lower()
                if decision in yes_no:
                    break
            if decision == 'ano' or decision == 'a':
                while True:
                    decision = input(color.BLUE + 'Skořápkář: ' + color.RESET + 'Zdarec kábre. Hra stojí tři pětky. Pokud uhodneš, dostaneš zpět dvojnásobek. (ano/ne): ').lower()
                    if decision in yes_no:
                        break
                while True:
                    if decision == 'ano' or decision == 'a':
                        if stats['money'] >= 30:
                            print(color.BLUE + 'Skořápkář: ' + color.RESET + 'Fajn. Dám kuličku pod jeden z kelímků. Pokud uhodneš pod kterým je, dostaneš zpět dvojnásobek')
                            time.sleep(5)
                            print(color.YELLOW + 'Skořápkář vkládá kuličku a míchá kelímky' + color.RESET)
                            i = 0
                            while i <= 5:
                                print('.',sep=' ',end='',flush=True)
                                i += 1
                                time.sleep(1)
                            while True:
                                decision = int(input('\n1▋  2▋  3▋\n' + color.BLUE + 'Skořápkář: ' + color.RESET + 'Který kelímek vybíráš? (1/2/3): '))
                                if decision in range(1,4):
                                    break
                            if decision == random.randint(1,3):
                                print(color.BLUE + 'Skořápkář: ' + color.RESET + 'Tak to jsem ještě nežral. DObrej tip!')
                                stats['money'] += 30
                                print_stats()
                                time.sleep(5)
                                while True:
                                    decision = input(color.BLUE + 'Skořápkář: ' + color.RESET + 'Dáme ještě jednu hru? (ano/ne): ')
                                    if decision in yes_no:
                                        break
                                break
                            else:
                                print(color.BLUE + 'Skořápkář: ' + color.RESET + 'Ha, blbej cajzle! Davaj!')
                                stats['money'] -= 30
                                print_stats()
                                time.sleep(5)
                                while True:
                                    decision = input(color.BLUE + 'Skořápkář: ' + color.RESET + 'Dáme ještě jednu hru? (ano/ne): ')
                                    if decision in yes_no:
                                        break
                                break
                        else:
                            print(color.BLUE + 'Skořápkář: ' + color.RESET + 'Sorry, tohle asi nezacáluješ. Nemáš dost bakulí.')
                            stats['sanity'] -= 2
                            print_stats()
                            break
                    elif decision == 'ne' or decision == 'n':
                        decision_from_cycle = 1
                        break
            if decision == 'ne' or decision == 'n' or decision_from_cycle == 1:
                print(color.YELLOW + 'Ty moc neriskuješ, co? Pražáci... Pojď, jdem na šalinu. Podíváme se do centra.')
                tram_to_centre()
        elif decision == 'konečná' or decision == 'k' or decision == 'konecna':
            print(color.YELLOW + 'Hmm. Trolejbus číslo 31. Někam za Brno. To raději riskovat nebudeme, co? Tady vede cesta zpět k nádru...' + color.RESET)
            time.sleep(5)
            near_train_station()

def tram_to_centre():
    pass

def tram_to_faculty():
    pass

def petrov():
    pass

near_train_station()