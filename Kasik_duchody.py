'''
Vaším cílem bude vytvořit nástroj pro správu výplat důchodů. Protože pracujete pro státní správu, tak by použítí databáze bylo příliš fancy.
Proto budete používat obyčejný textový soubor s informacemi o lidech, kteří mají dostávat důchod. Tento soubor se jmenuje duchodci.csv

Struktura souboru duchodci.csv je nasledujici:
ID;Jméno;Příjmení;Ulice;Číslo popisné nebo orientační;Město;PSČ;Lokalizace(ve WKT);Výše důchodu

Př.
1;Gabriel;Douša;Žižkova;204;Určice;79804;POINT(49.430556, 17.073056);11500

Jedná se o citlivá data, proto je nutné logovat veškeré změny a přístupy k těmto datům. Proto každou operaci, kterou provedete (čtení, modifikace, vytvoření) 
zalogujete do souboru operace.log. Záznam v logu bude vypadat následovně:

Datum
Typ operace: (čtení, vytvoření, modifikace)
ID záznamu: Id záznamu
Status: např. OK pokud operace proběhla, jinak text výjimky nebo vámi zapsaná chyba

Př.
2020-12-22 11:28:13.010271
Typ operace: čtení
ID záznamu: 1
Status: strukturu nechám na vás

Za každým záznamem bude pro přehlednost vynechaný řádek

Implementujte tyto funkce (NENÍ TŘEBA IMPLEMENTOVAT ROZHRANÍ - volejte si jen funkce):
1. Vyhledání konkrétního důchodce/ů podle jména (stačí zadat křestní jméno nebo jen příjmení)
2. Přidání nového záznamu do souboru duchodci.csv
3. Změna bydliště pro konkrétní osobu
4. Výplata důchodů - vyplaťte virtuální důchody. 
    Zapište do logu zda výplata proběhla a pokud nastala chyba, tak ji zapište také (mohlo nastat pokud je záznam chybný - nemá výši důchodu)
5. Valorizace důchodů - zvyšte všechny důchody o 5 %

Každá z funkcí bude zalogovaná do souboru operace.log podle výše zmíněné struktury
Pokud nastane nějaká chyba (např. záznam, který chcete modifikovat nebude existovat nebo záznam nebude mít výši důchodů tak zapište odpovídající chybu do logu)

Kód strukturujte podle svého uvážení. Bude se hodnotit i kvalita kódu a jeho přehlednost.
'''
import geocoder, datetime

persons = []
properties = ['name', 'surname', 'street', 'house number', 'city', 'postal code', 'geometry', 'pension']
log_event_id = 1

with open('duchodci.csv', mode='r', encoding='utf8') as retired_persons:
    count = 0
    for line in retired_persons:
        line_split = line.split(';')
        line_split[-1] = line_split[-1].strip()
        persons.append(line_split)
        count += 1

def person_lookup(surname):
    for sublist in persons:
        if sublist[2] == surname:
            print('Person found!')
            log_file_print(1, 'OK', sublist[0])
            return sublist
    print('Person not found!')
    log_file_print(1, 'FAILED', None)

def add_person():
    new_person = [count + 1]
    for property in properties:
        if property != 'geometry':
            value = input('Insert ' + property + ': ')
        else:
            coordinates = geocoder.osm(new_person[5]).latlng
            value = 'POINT(' + str(coordinates[0]) + ', ' + str(coordinates[1]) + ')'
        new_person.append(value)
    persons.append(new_person)
    print('New person successfully added!')
    log_file_print(2, 'OK', count)

def change_adress(surname):
    for sublist in persons:
        if sublist[2] == surname:
            sublist[3] = input('New street: ')
            sublist[4] = input('New house number: ')
            sublist[5] = input('New city: ')
            sublist[6] = input('New postal number: ')
            coordinates = geocoder.osm(sublist[5]).latlng
            sublist[7] = 'POINT(' + str(coordinates[0]) + ', ' + str(coordinates[1]) + ')'
            log_file_print(3, 'OK', sublist[0])
            return print('Adress successfully changed!')
    

def pay_out():
    for person in persons:
        if len(person[-1]) > 0:
            # pension payed
            log_file_print(4, 'OK', person[0])
        else:
            # pension amount not found
            log_file_print(4, 'FAILED', person[0])

def pension_raise():
    for person in persons:
        if len(person[-1]) > 0:
            person[-1] = float(person[-1]) * 1.05
            log_file_print(5, 'OK', person[0])
        else:
            log_file_print(5, 'FAILED', person[0])

with open('log_file.txt', mode='w', encoding='utf8') as logfile:
        logfile.write('Types of operations:\n1 -> Person search\n2 -> Add person\n3 -> Change adress\n4 -> Pension payout\n5 -> Pension raise by 5 %\n\n')

def log_file_print(operation, status, person_id):
    with open('log_file.txt', mode='a', encoding='utf8') as logfile:
        logfile.write(str(datetime.datetime.now()) + '\nOperation: ' + str(operation) + '\nLog event id: ' + str(log_event_id) + '\nPerson id: ' + str(person_id) +'\nStatus: ' + status + '\n\n')

#person_lookup(input('Input surname for search: '))
#add_person()
#change_adress(input('Insert surname to change adress: '))
pay_out()
pension_raise()

with open('duchodci.csv', mode='w', encoding='utf8') as persons_file:
    for person in persons:
        delimiter = ';'
        output_string = ''
        count = 0
        for i in person:
            output_string = output_string + str(i)
            if count < 8:
                output_string = output_string + delimiter
            count += 1
        output_string = output_string + '\n'
        persons_file.write(output_string)
