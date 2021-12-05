# vytvorte funkci, ktera bude mit jako jediny vstupni parametr slovnik
# funkce slovnik pouze vypise
# Pokud nebude jako parametr zadan slovnik, ale jiny datovy typ, tak funkce vyhodi vyjimku TypeError
test_dictionary = {'pes' : 'haf'}
test_number = 21 


def print_dictionary(actual_dictionary):
    print(actual_dictionary)

try:
    print_dictionary(dict(test_number))
except TypeError:
    print('Na vstupu funkce není slovník!')
