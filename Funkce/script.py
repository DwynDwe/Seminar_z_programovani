""" def sum(n1, n2):
    sum = n1 + n2
    return sum

print(sum(5, 8)) 

def sum1(numbers):
    addition = 0
    for i in numbers:
        addition += i
    return addition

list = [1, 5, 8, 10, 7, 19]

print(sum1(list))

def concate(*args):
    print(args)

concate('Tvoje máma', 8, 'nuggetka')


def sum2(*args):
    addition = 0
    for i in args:
        addition += i
    return addition

print(sum2(1, 8, 88, 98, 74, 55, 667))"""

def unique(values):
    return set(values)


print(unique([1, 1, 1, 8, 4, 'Marek', 'Ivo', 'Marek']))