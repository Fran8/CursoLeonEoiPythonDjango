"""ejemplos de funciones simples
"""
def hi():
    print('hola')

hi()

def hi_to(name):
    print('hi', name)

hi_to('Ramon')

def add_name(name_list, name):
    name_list.append(name)
    print(name_list)

l = ['Patricia','Mahria']
add_name(l,'Carlota')

def talk(word):
    word='cambio'
    print(word)
    