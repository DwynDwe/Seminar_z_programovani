from random import choice

colors = ['red','orange','green']
color_light = choice(colors)

print('Barva semaforu je:', color_light)
if color_light == 'red':
    print('Auta stojí.')
elif color_light == 'orange':
    print('Auta se rozjíždějí!')
else:
    print('Auta jedou!')