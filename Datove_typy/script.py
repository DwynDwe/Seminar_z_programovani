from typing import final


my_name = "Daniel Kašík"
name = "Daniel"

print(my_name, name)
print(name.lower())

decision = True

empty = None

print(type(empty))
print(type(name))

num = "20"
print("Typ proměnné num: ", type(num))
new_num = int(num)
print("Typ proměnné new_num: ", type(new_num))


print("Vynásobím co chceš!")
num = int(input("Zadej první číslo: "))
num2 = int(input("Zadej druhé číslo: "))
addition = num + num2
substract = num - num2
multiply = num * num2
divide = num / num2
print("Součet: ", addition, " Odečítání: ", substract, " Násobení: ", multiply, " Dělení: ", divide)

print("Délka jména: ", len(name))

print("Poslední písmeno jména: ", name[-1])

name = name.replace("Daniel", "Radim")
name = name.split("d")
print("Zrádce: ", name)

