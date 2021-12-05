# zapiste do souboru 5 jmen
# jmena nasledne vypiste
# pridejte do souboru dalsi 2 jmena
# nakonec jmena prectete a zapiste do jineho souboru
first_names = ['Alžbeta', 'Mikuláš', 'Celestýn', 'Emanuel', 'Eleanor']
second_names = ['Zikmund', 'Ofélie']

def read_names():
    with open('first_names.txt', encoding='utf8', mode='r') as file:
        for line in file:
           print(line)

def write_names(namelist, mode_type):
    with open('first_names.txt', encoding='utf8', mode=mode_type) as file:
        for name in namelist:
            file.write(name + '\n')

def copy_names():
    with open('final_names.txt', encoding='utf8', mode='w') as new_file:
        with open('first_names.txt', encoding='utf8', mode='r') as original_names:
            for name in original_names:
                new_file.write(name)

write_names(first_names, 'w')
read_names()
print('-----------')
write_names(second_names, 'a')
read_names()
print('-----------')
copy_names()


