# vytvorte funkci, ktera bude mit na vstupu libovolny pocet cisel
# tyto cisla vypise v libovolnem formatu jen tehdy pokud je kazde cislo vyssi nez 10
# pokud nektere z cisel bude mensi nez 10, tak funkce vyhodi vyjimku ValueError s libovolnou hlaskou

import random

def number_check(list):
    for number in list:
        if number <= 10:
            raise ValueError('Číslo na vstupu je menší nebo rovno 10!')
    return(list)

random_list = []
for number in range(random.randint(1,20)):
    random_list.append(random.randint(0,100))

print(number_check(random_list))