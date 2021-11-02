from colorama import Fore as color
import time, random, threading
from playsound import playsound

stats = {
    'health' : 5,
    'sanity' : 5,
    'money' : 100
}

world_parties = ['sever','s','jih','j','západ','z','zapad','východ','v','vychod']
yes_no = ['ano','ne','a','n']
end_station = ['podchod','p','konečná','k','konecna']
petrov_decision = ['hlavák','hlavak','h','nové sady','nove sady','n']
abcd = ['a','b','c','d']
question_bank = ['První otázka, jo. Který z uvedených geologických procesů je nejmladší?\na) udazování křídových sedimentů v České křídové tabuli\nb) usazování vápenců Českého krasu\nc) vyvrásnění Karpat\nd) vyvrásnění Krkonoš\nOdpověď (a/b/c/d): ', 'Druhá, jo. Který z uvedených regionů se nenachází na území Evropské unie?\na) Baskicko\nb) Toskánsko\nc) Vojvodina\nd) Korutansko\nOdpověď (a/b/c/d): ', 'Třetí otázka, jo. Ve kterém z uvedených měst bude 5. července nejdelší den?\na) Riga\nb) Vídeň\nc) Quito\nd) Montevideo\nOdpověď (a/b/c/d): ', 'Dál, jo. Jaké je měřítko mapy, jestliže vzdálenost dvou měst, která ve skutečnosti činí 20 km, je na této mapě 4 cm?\na) 1 : 80 000\nb) 1 : 200 000\nc) 1 : 500 000\nd) 1 : 800 000\nOdpověď (a/b/c/d): ', 'A poslední, jo. Vyberte CHKO, ve které se nenachází přiřazený přírodní jev:\na) MOravský kras -> jeskyně\nb) Litovelské Pomoraví -> lužní les\nc) Broumovsko -> pískovcové skály\nd) Žďárské vrchy -> karová jezera\nOdpověď (a/b/c/d): ']
question_bank_answers = ['c', 'c', 'a', 'c', 'd']
herber_reaction_positive, herber_reaction_negative = ['Fajn, to by šlo, jo.', 'Nejsi úplně blbej, jo.', 'Že by budoucí geograf?', 'Hmmm, dobrý.', 'Fajn, fajn!', 'Pěkně'], ['No to asi ne, jo.', 'Hehe, nene.', 'To byla jedna z jednodušších, jo.', 'Fakt chceš přežít, jo?']
kidnaping = False

def print_stats():
    print('zdraví: ' + str(stats['health']) + '\npříčetnost: ' + str(stats['sanity']) + '\npeníze: ' + str(stats['money']))

def start():
    decision = input(color.YELLOW + 'Vítej v Brně! Ve městě, kde je možné všechno. A že je to fakt drsný místo, dokládají i novinové titulky:\n' + color.BLUE + '25. července 2021:' + color.RESET + ' Muž v parku v Brně tvrdil, že je král a máchal okolo sebe šroubovákem\n' + color.BLUE + '27. června 2021: ' + color.RESET +'Muž v prodejně v Brně přelepil mixér a reproduktor cenovkami zeleniny\n' + color.BLUE + '18. března 2018: ' + color.RESET + 'Přijel z Chebu na návštěvu do Brna, útočník mu ukousl nos\n' + color.YELLOW + 'Ještě je čas utéct. Chceš určitě zůstat? (ano/ne): ' + color.RESET).lower()
    print('\n')
    if decision == 'ano' or decision == 'a':
        print(color.YELLOW + 'Výborně! Vydejme se na dobrodružství! Toto jsou tvoje statistiky:\n' + color.RESET + 'zdraví: ' + str(stats['health']) + '\npříčetnost: ' + str(stats['sanity']) + '\npeníze: ' + str(stats['money']))
        time.sleep(7)
        print(color.YELLOW + 'Tyto statistiky jsou důležité pro tvé přežití. Nikdy se nesmí dostat na nulu. Nechceš přece, aby do tebe vrtal nějakej brněnskej felčar pazourkem. Každý úkol, který před tebou bude stát, ti při špatném vyřešení může ubrat některý z atributů. Tvé statistiky se objeví vždy, když dostaneš nějaké poškození (nebo za něco zaplatíš). Pokud se budeš muset rozhodnout, lze odpovědět jedním z textů v závorce. Lze použít i jen počáteční písmeno odpovědi. Doporučuju mít zapnutý zvuk. A teď vzhůru do Brna!\n' + color.RESET)
        time.sleep(10)
        train_station()
    else:
        print(color.YELLOW + 'Srabe. Támhle ti jede écéčko do Prahy.' + color.RESET)
        gameover_crash()
        time.sleep(5)
        print(color.RED + '\n***GAME OVER***' + color.RESET)
        time.sleep(5)

def train_station():
    print(color.YELLOW + 'Jedna z nejhezčích brněnských budov. Společně s břeclavským nádrem nejstarší v zemi. Ale koho zajímá Břeclav. Navíc - máme tu bezdomovce a ti prostě patří k našemu koloritu. Hele, jeden přichází!' + color.RESET)
    print(color.BLUE + 'Bezdomovec:' + color.RESET + ' Čááu. Nemáš prosimtě ňáky bakule?')
    decision = input(color.YELLOW + 'Moc nechápeš, co po tobě chce, co? Hele, natahuje ruku! To bude chtít asi prachy! Dáš mu dvacku? (ano/ne): ' + color.RESET).lower()
    if decision == 'ano' or decision == 'a':
        print(color.BLUE + 'Bezdomovec: ' + color.RESET + 'Díky šéfe! Máte dobrý srdéčko\n\n' + color.YELLOW + 'Tak to proběhlo celkem hladce. Honem před budovu. Vypadá to, že se k tobě ženou další!\n'+ color.RESET)
        stats['money'] -= 20
        print_stats()
        near_train_station()
    else:
        print(color.BLUE + 'Bezdomovec: ' + color.RESET + 'Bleehhh\n\n' + color.YELLOW + 'Hehe. To jsi asi nečekal. Být hned po výstupu nahozenej bezdomovcem. To chceš. Běž radši rychle ven, než se stane něco dalšího.' + color.RESET)
        stats['sanity'] -= 2
        stats['health'] -= 1
        print_stats()
        near_train_station()

def near_train_station():
    time.sleep(5)
    while True:
        decision = input(color.YELLOW + 'Rušný místo. Spousta lidí se hrne přes sebe, ženou se na šaliny a trajfy. Co? Jo - trolejbusy. Bože.\nHlavas je prostě šíleně důležitý místo v Brně. Přes den se tu všechno děje a v noci, v noci vlastně taky. Tak kam teď? (sever, jih, západ, východ): ' + color.YELLOW).lower()
        if decision in world_parties:
            break
    if decision == 'sever' or decision == 's':
        print(color.YELLOW + 'Takže k šalině. Rovnou na věc. Pojeďme z toho drsnýho hlaváku přímo do štatlu - tam přežiješ dýl jak deset minut.' + color.RESET)
        time.sleep(3)
        tram_to_centre()
    elif decision == 'jih' or decision == 'j':
        print(color.YELLOW + 'Vracet se na nádr? Jsi vyměkl, srabe? Teď už necouvneš. Zkus to znovu!' + color.RESET)
        time.sleep(3)
        near_train_station()
    elif decision == 'západ' or decision == 'z' or decision == 'zapad':
        nove_sady()
    elif decision == 'východ' or decision == 'v' or decision == 'vychod':
        while True:
            decision = input(color.YELLOW + 'Nějaká konečná trolejbusu. A podchod. Kam teď? (podchod/konečná): ' + color.RESET).lower()
            if decision in end_station:
                break
        if decision == 'podchod' or decision == 'p':
            decision = None
            decision_from_cycle = 0
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
                                stats['money'] += 60
                                print_stats()
                                time.sleep(5)
                                while True:
                                    decision = input(color.BLUE + 'Skořápkář: ' + color.RESET + 'Dáme ještě jednu hru? (ano/ne): ')
                                    if decision in yes_no:
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
                time.sleep(5)
                tram_to_centre()
        elif decision == 'konečná' or decision == 'k' or decision == 'konecna':
            print(color.YELLOW + 'Hmm. Trolejbus číslo 31. Někam za Brno. To raději riskovat nebudeme, co? Tady vede cesta zpět k nádru...' + color.RESET)
            time.sleep(5)
            near_train_station()

def tram_to_centre():
    print(color.YELLOW + 'Šalina pomalu jede po Masaryčce. Vidíš všechny ty krásné obchůdky?' + color.RESET)
    time.sleep(3)
    print(color.YELLOW + 'Sakra! Revizor!' + color.RESET)
    tram_inspector()
    time.sleep(3)
    print(color.YELLOW + 'To zas bylo něco. Ale tak nějaký peníze ještě máš. Přežít ve štatlu, když jsi blbec, není jednoduchý...' + color.RESET)
    time.sleep(4)
    print(color.YELLOW + 'CO TO ZAS JE? POVOZ?!' + color.RESET)
    playsound('Podminky\\tram_ring.mp3')
    print(''.join(random.choice('*\\#@{}]Đđ_-') for character in range(1000)))
    print('\nTMA')
    if stats['health'] <= 4:
        stats['health'] = 0
        gameover_stats()
    else:
        herber_kidnaping()

def tram_to_faculty():
    print(color.YELLOW + 'Kolem Petrova do hroznýho kopce. A ti šmirgláci tu jezdí jak magoři...' + color.RESET)
    time.sleep(3)
    print(color.YELLOW + 'Sakra. Revizor!' + color.RESET)
    tram_inspector()
    print(color.YELLOW + 'To zas bylo něco. Ale tak nějaký peníze ještě máš. Přežít ve štatlu, když jsi blbec, není jednoduchý...' + color.RESET)
    time.sleep(5)
    while True:
        decision = input(color.YELLOW + 'Pokud chceš, aby tě Brno vzalo za svý, musíš se tu buď narodit, nebo tu začít studovat. Nechceš zkusit Přírodovědu? Zrovna kolem ní jedeme... (ano/ne): ' + color.RESET).lower()
        if decision in yes_no:
            break
    if decision == 'ano' or decision == 'a':
        print(color.YELLOW + 'Super! Tak dem.' + color.RESET)
        time.sleep(3)
        herber_quiz()
    else:
        print(color.YELLOW + 'Už mě nebaví ty tvoje výmluvy. Že to se ti nechce a támto se ti nechce! Hybaj!')
        time.sleep(4)
        herber_quiz()

def petrov():
    print(color.YELLOW + 'Fajn místo. Drogy tu seženeš. A taky tu je čupr výhled.' + color.RESET)
    time.sleep(3)
    while True:
        decision = input(color.YELLOW + 'Co se rozhlídnout kam dál? (ano/ne): ' + color.RESET).lower()
        if decision in yes_no:
            break
    if decision == 'ano' or decision == 'a':
        print(color.YELLOW + 'Je tu pekný výhled, co? Celý jih jako na dlani. NENAHÝBEJ SE!' + color.RESET)
        time.sleep(5)
        print(''.join(random.choice('*\\#@{}]Đđ_-') for character in range(1000)))
        print('\n*****TMA*****')
        gameover_crash()
    else:
        while True:
            decision = input(color.YELLOW + 'Tak kam teď? (Hlavák/Nové sady): ' + color.RESET).lower()
            if decision in petrov_decision:
                break
        if decision == 'hlavak' or decision == 'hlavák' or decision == 'h':
            near_train_station()
        else:
            nove_sady()

def nove_sady():
    time.sleep(5)
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

def tram_inspector():
    while True:
        decision = input(color.BLUE + 'Revizor: ' + color.RESET + 'Dobrý den, kontrola jízdenek. Máte jízdenku? (ano/ne): ').lower()
        if decision in yes_no:
            break
    if decision == 'ano' or decision == 'a':
        print(color.BLUE + 'Revizor: ' + color.RESET + 'A ukážete mi ji?')
        time.sleep(3)
        print(color.YELLOW + 'Opravdu si myslíš, že když budeš dělat, že ji hledáš, že tě pustí? Vím, že sis žádnou nekoupil.' + color.RESET)
        time.sleep(3)
        print(color.BLUE + 'Revizor: ' + color.RESET + 'Takže nemáte? To bude mastný.')
        time.sleep(3)
        print(color.YELLOW + 'Jseš blbej no. Nenapadlo mě, že pražáci si nekupují lístky na socku.' + color.RESET)   
        time.sleep(3)
        stats['money'] -= 70
        if stats['money'] <= 0:
            gameover_stats()
        print_stats()
    else:
        print(color.BLUE + 'Revizor: ' + color.RESET + 'Takže nemáte? To bude mastný.')
        time.sleep(3)
        print(color.YELLOW + 'Jseš blbej no. Nenapadlo mě, že pražáci si nekupují lístky na socku.' + color.RESET)   
        time.sleep(3)
        stats['money'] -= 70
        if stats['money'] <= 0:
            gameover_stats()
        print_stats()

def herber_kidnaping():
    global kidnaping
    kidnaping = True
    time.sleep(5)
    print(color.BLUE + 'Brněnská napodobenina papeže: ' + color.RESET + 'Těžký časy v Brně, jo? Máš štěstí, že žiješ, jo. Ale zadarmo nedělám, jo. Dám ti pět otázek, jo. Pokud, jo, na alespoň čtyři odpovíš správně, jo, tak tě pustím a raději pošlu zpátky do Prahy, jo? Pokud to nedáš, jo, tak tě dorazím, jo?')
    herber_quiz()

def herber_quiz():
    time.sleep(10)
    if kidnaping == False:
        print(color.BLUE + 'Brněnská napodobenina papeže: ' + color.RESET + 'Vítejte, jo,  na naší fakultě! Z důvodů všech možných dopravních uzavírek v Brně, jo, je jediné smysluplné studium kartografie, jo. Jinak, jo, nevíme kudy kam. Dostanete pět otázek, jo. Pro přijetí, jo, je potřeba zodpovědět alespoň čtyři správně.\n')
    else:
        print(color.BLUE + 'Brněnská napodobenina papeže: ' + color.RESET + 'Nemáš vlastně na výběr, jo.\n')
    time.sleep(6)
    correct, count = 0, 0
    for question in question_bank:
        while True:
            decision = input(color.BLUE + 'Brněnská napodobenina papeže: ' + color.RESET + question).lower()
            if decision in abcd:
                break
            else:
                print('To není ani na výběr')
        if decision == question_bank_answers[count]:
            print(color.BLUE + 'Brněnská napodobenina papeže: ' + color.RESET + random.choice(herber_reaction_positive))
            correct += 1
        else:
            print(color.BLUE + 'Brněnská napodobenina papeže: ' + color.RESET + random.choice(herber_reaction_negative))
        count += 1
        time.sleep(3)
        print('\n')
    if correct >= 4:
        if kidnaping == True:
            gameover_herber_train()
        else:
            gamewin()
    else:
        if kidnaping == True:
            gameover_herber_kill()
        else:
            gameover_herber_train()

def gameover_crash():
    sound_thread = threading.Thread(target=gameover_sound)
    sound_thread.daemon = True
    sound_thread.start()

def gameover_sound():
    playsound('Podminky\\crash_gameover.mp3', block=False)

def gameover_herber_kill():
    time.sleep(6)
    gameover_crash()
    print(color.BLUE + '\nBrněnská napodobenina papeže: ' + color.RESET + 'Nešťastné, jo. Nepatříš ani k těm chytřejším.')
    stats['sanity'] = 0
    time.sleep(3)
    print_stats()
    time.sleep(6)
    print(color.BLUE + '\nBrněnská napodobenina papeže: ' + color.RESET + 'Ještě peníze prosím, jo.')
    stats['money'] = 0
    time.sleep(3)
    print_stats()
    time.sleep(6)
    print(color.BLUE + '\nBrněnská napodobenina papeže: ' + color.RESET + 'Asi se rozloučíme, jo.\n')
    time.sleep(6)
    print(''.join(random.choice('*\\#@{}]Đđ_-') for character in range(1000)))
    stats['health'] = 0
    time.sleep(3)
    print_stats()
    time.sleep(6)
    print(color.RED + '\n***GAME OVER***' + color.RESET)

def gameover_herber_train():
    time.sleep(5)
    gameover_crash()
    print(color.BLUE + '\nBrněnská napodobenina papeže: ' + color.RESET + 'Takový tu úplně nechceme, jo. Jeď prosím zpět do Prahy, než se ti něco stane.')
    time.sleep(5)
    print(color.RED + '\n***GAME OVER***' + color.RESET)

def gameover_stats():
    time.sleep(3)
    print(color.YELLOW + 'Nedošlo ti něco?' + color.RESET)
    time.sleep(3)
    print_stats()
    time.sleep(3)
    print(color.YELLOW + 'Tak z Brna se už očividně nikdy nedostaneš...' + color.RESET)
    gameover_crash()
    time.sleep(5)
    print(color.RED + '\n***GAME OVER***' + color.RESET)
    time.sleep(5)

def gamewin():
    time.sleep(5)
    print(color.YELLOW + 'Takže budoucí student! Gratuluju! Snad tě teď Brno už nesežere :)')
    time.sleep(6)
    print(color.GREEN + '\n+++VÍTĚŽSTVÍ+++' + color.RESET)

start()