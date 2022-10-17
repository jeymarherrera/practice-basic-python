demoList = [1, 'hello', 1.23, True, [1,2,3]]
colors = ['Amarillo', 'Azul', 'Verde']

#constructor
numbersList=list((1,2,3,4))

print(demoList)
print(numbersList)

r = list(range(1,10))
print(r)

print('Azul' in colors)
print(colors)

#cambiar valores
colors[1] = 'Morado'
print(colors)

colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)

colors.append('Negro')
colors.append(('Rojo', 'Dorado'))
colors.append(['Blanco', 'Marrón', 'Gris'])
colors.extend(['Naranja', 'Vinotinto'])
colors.insert(1, 'Canela')
colors.insert(len(colors), 'Green')
print(colors)

colors.pop() #elimina indice o ultimo elemento
print(colors)

colors.remove('Vinotinto')
print(colors)

print(colors.index("Verde"))

print(colors.count("Canela"))

colors.clear()
print(colors)