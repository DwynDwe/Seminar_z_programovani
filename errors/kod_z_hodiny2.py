# starsi zpusob - moc nepouzivat
file = open('06-vyjimky_a_prace_se_soubory\\soubor.txt')
print(file.read())
print(file.readline()) 
file.close()

with open('06-vyjimky_a_prace_se_soubory\\soubor.txt', encoding='utf8', mode='r') as file:
    # print(file.encoding)
    for line in file:
        print(line)
print('soubor je zavreny')

# mode='r'
# mode='a'
# mode='w'
with open('06-vyjimky_a_prace_se_soubory\\soubor.txt', encoding='utf8', mode='a') as file:
    file.write('neco tu zapisu')

with open('06-vyjimky_a_prace_se_soubory\\soubor.txt', encoding='utf8', mode='r+') as file:
    file.write('neco tu zapisu')
    file.write('neco tu zapisu2')
