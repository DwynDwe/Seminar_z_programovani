""" def division(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError('Dělení nulou')
    return num1/num2

print(division(1,1))
print(division(1,0)) """

""" import traceback

try:
    div = 1/0
except (ZeroDivisionError, IndexError):
    print('Tvoje máma je nula')
except IndexError:
    print('Tvoje máma je index')
except:
    print('Tvoje máma je obecná chyba')
finally:
    print('Tvoje máma') """

file = open('errors\\file.txt')
print(file.readline())
