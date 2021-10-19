from colorama import Fore as color
import time

stats = {
    'health' : 5,
    'sanity' : 5,
    'money' : 100
}

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
    decision = None
    while decision == None:
        decision = input(color.YELLOW + 'Rušný místo. Spousta lidí se hrne přes sebe, ženou se na šaliny a trajfy. Co? Jo - trolejbusy. Bože.\nHlavas je prostě šíleně důležitý místo v Brně. Přes den se tu všechno děje a v noci, v noci vlastně taky. Tak kam teď? (sever, jih, západ, východ): ' + color.YELLOW).lower()
        if decision == 'sever' or decision == 's':
            decision = None
            pass
        elif decision == 'jih' or decision == 'j':
            decision = None
            pass
        elif decision == 'západ' or decision == 'z' or decision == 'zapad':
            decision = None
            pass
        elif decision == 'východ' or decision == 'v' or decision == 'vychod':
            decision = None
            while decision == None:
                decision = input(color.YELLOW + 'Nějaká konečná trolejbusu. A podchod. Kam teď? (podchod/konečná): ' + color.RESET).lower()
                if decision == 'podchod' or decision == 'p':
                    decision = None
                    print(color.YELLOW + 'Temný místo. Patrioti tomu říkaj Myší díra. Vede většinou na nástupiště emhádéčka. Občas se tam někdo ztratí... Tak jdem.' + color.RESET)
                    time.sleep(5)
                    while decision == None:
                        decision = input(color.YELLOW + 'Hele, skořápky! Pojď, zahrajem si! (ano/ne): ' + color.RESET).lower()
                        if decision == 'ano' or decision == 'a':
                            decision = None
                            while decision == None:
                                decision = input(color.BLUE + 'Skořápkář: ' + color.RESET + 'Zdarec kábre. Hra stojí tři pětky. Pokud uhodneš, dostaneš zpět dvojnásobek. (ano/ne): ').lower()
                                if decision == 'ano' or decision == 'a':
                                    pass
                                elif decision == 'ne' or decision == 'n':
                                    pass
                                else:
                                    decision = None
                        elif decision == 'ne' or decision == 'n':
                            pass
                        else:
                            decision = None
                elif decision == 'konečná' or decision == 'k' or decision == 'k':
                    print(color.YELLOW + 'Hmm. Trolejbus číslo 31. Někam za Brno. To raději riskovat nebudeme, co?' + color.RESET)
                    decision = None
                else:
                    decision = None
        else:
            decision = None

near_train_station()