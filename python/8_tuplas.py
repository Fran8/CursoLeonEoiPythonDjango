""" ejemplos para trabajar con tuplas 
"""
# las tuplas no pueden modificarse, pero pesan menos

# control + F2 para seleccionar la misma palabra en todos los lados y poder modificarla
TUP = (1, 2, 3, 4, 5, "seis")

print(TUP)
print(TUP[0])
print(TUP[4])
print(TUP[2:5])
print(TUP[:3])
print(TUP[2:])

size = len(TUP)
print('tamaño de la lista', size)

# concatenar listas
TUP += ('siete', 8, True, False)
print(TUP)

SUMA = (3 + 2) -1

T2 = (3,)
print(T2)
print(type(T2))







