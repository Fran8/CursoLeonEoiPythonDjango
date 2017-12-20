""" ejemplos para trabajar con listas 
"""
# control + F2 para seleccionar la misma palabra en todos los lados y poder modificarla
LIST = [1, 2, 3, 4, 5, "seis"]

print(LIST)
print(LIST[0])
print(LIST[4])
print(LIST[2:5])
print(LIST[:3])
print(LIST[2:])

size = len(LIST)
print('tamaño de la lista', size)

del LIST[2]
print(LIST)

LIST[2] = "tres"
print(LIST)

# concatenar listas
LIST += ['siete', 8, True, False]
print(LIST)

# añadir elemento a la lista
LIST.append('elemento nuevo')
print(LIST)

LIST.remove('seis')
print(LIST)

LIST.reverse()
print(LIST)

LIST.insert(4, 'PC')
print(LIST)



