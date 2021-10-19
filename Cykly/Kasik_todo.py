from colorama import Fore as color
import datetime

print('---------Zápisníček---------')

list = [{'text': 'Naprogramovat textovou hru', 'deadline': datetime.date(2021, 11, 2), 'done': 0},{'text': 'Koupit šalinkartu', 'deadline': datetime.date(2021, 10, 18), 'done': 1},{'text': 'Odeslat maily do práce', 'deadline': datetime.date(2021, 11, 15), 'done': 0},{'text': 'Koupit kabát', 'deadline': datetime.date(2021, 11, 16), 'done': 1}]
new_note_keys = ['text','deadline','done']
new_note = dict.fromkeys(new_note_keys)
today = datetime.date.today()

while True:
    user_choice = int(input('Vyberte akci.\n1 = Vložit nový úkol\n2 = Zobrazit úkoly po deadlinu\n3 = Zobrazit všechny úkoly\n4 = Splnit poznámku\n5 = Ukončit zápisníček\nVýběr: '))
    if user_choice == 1:
        new_text = str(input("Text úkolu: "))
        date_input = str(input('Zadejte deadline ve formátu DD-MM-RRRR: '))
        day, month, year = map(int, date_input.split('-'))
        new_deadline = datetime.date(year, month, day)
        new_note['text'] = new_text
        new_note['deadline'] = new_deadline
        new_note['done'] = 0
        list.append(new_note)
        print('Poznámka úspěšně vytvořena')
    elif user_choice == 2:
        missed_counter = False
        for i in list:
            if i['deadline'] < today and i['done'] == 0:
                print('Nesplněné úkoly s proměškaným deadlinem:\n', i['deadline'], ' ', i['text'])
                missed_counter = True
        if missed_counter == False:
            print('Žádné zmeškané úkoly')
    elif user_choice == 3:
        print('Všechny úkoly:')
        for i in list:
            if i['deadline'] < today:
                if i['done'] == 0:
                    print(color.RED + str(i['deadline']) + color.RESET + ' ' + i['text'] + color.RED + ' ' + 'NESPLĚNO' + color.RESET)
                else:
                    print(color.RED + str(i['deadline']) + color.RESET + ' ' + i['text'] + color.GREEN + ' ' + 'SPLNĚNO' + color.RESET)
            elif i['deadline'] > today:
                if i['done'] == 0:
                    print(color.GREEN + str(i['deadline']) + color.RESET + ' ' + i['text'] + color.YELLOW + ' ' + 'NESPLĚNO' + color.RESET)
                else:
                    print(color.GREEN + str(i['deadline']) + color.RESET + ' ' + i['text'] + color.GREEN + ' ' + 'SPLNĚNO' + color.RESET)
    elif user_choice == 4:
        while True:
            choice_counter = 0
            run = 1 #je to potřeba?
            for i in list:
                if i['done'] == 0:
                    choice_counter += 1
                    run -= 1
                    if i['deadline'] > today:
                        print(str(choice_counter) + ' = ' + color.GREEN + str(i['deadline']) + color.RESET + ' ' + i['text'] + color.YELLOW + ' ' + 'NESPLĚNO' + color.RESET)
                    elif i['deadline'] < today:
                        print(str(choice_counter) + ' = ' + color.RED + str(i['deadline']) + color.RESET + ' ' + i['text'] + color.RED + ' ' + 'NESPLĚNO' + color.RESET)
                elif choice_counter == 0 and run < 1:
                    print('Žádné úkoly ke splnění')
            if choice_counter != 0:
                user_choice = int(input('Který úkol chcete označit za splněný? '))
                if user_choice <= choice_counter:
                    break
                else:
                    counter_done = 1
                    for i in list:
                        if i['done'] == 0:
                            counter_done += 1
                            print(counter_done)
                            if counter_done == user_choice:
                                i['done'] = 1
                                break
        print('Hotovo')
    elif user_choice == 5:
        break
    else:
        print('Nerozpoznaná volba, prosím vyberte znovu.')
    
