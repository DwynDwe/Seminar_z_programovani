def division(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError('Dělení nulou')
    return num1/num2

print(division(1, 1))
print(division(1, 0))
 
try:
    div = 1/0
except (ZeroDivisionError, IndexError):
    print('Dělení nulou nebo chyba indexu')

import traceback

try:
    div = 1/0
    print('ahoj'[4])
except ZeroDivisionError:
    print('Dělení nulou')
    traceback.print_exc()
except IndexError as e:
    print('Chyba indexu')
    print(e)
except:
    print('Jakakoliv chyba')
finally:
    # vykona vzdycky
    print('vykona se vzdy')


