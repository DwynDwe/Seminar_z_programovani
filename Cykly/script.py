""" person = {'name': 'Standa', 'age': 22, 'city': 'Brno'}
for k,v in person.items():
    print(k, '->', v) """

""" list = ['pes','ovce','had']
while True:
    user = input('Mám doma toto zvíře? ').lower()
    if user in list:
        print('Ano, mám doma: ', user)
        break
    else:
        print('Tak tohle doma nemám!') """

""" list = [52, 58, 2, 22, 10, 101, 85, 77, 11, 28]
even = 0
odd = 0

for i in list:
    if i % 2 == 0:
        odd += 1
    else:
        even += 1

print('Licha: ', even, '\nSudá: ', odd)  """

dictionary1 = {"brand": "seat", "colour": "black", "price": 35000, "procento": 0.5}
dictionary2 = {"brand": "skoda", "colour": "red", "price": 77000, "procento": 0.8}
dictionary3 = {"brand": "ford", "colour": "white", "price": 65000, "procento": 2}

list = []

list.append(dictionary1)
list.append(dictionary2)
list.append(dictionary3)

for i in list:
    i['price'] += ((i['price'] / 100) * i['procento'])

print(list)