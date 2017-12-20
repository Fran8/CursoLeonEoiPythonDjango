"""
ejemplo del uso de expresiones regulares
"""
import re

phone = '666781809 # esto es un numero de telefono'

# borrar comentarios
number = re.sub(r'#.*$', '', phone)
print('Teléfono', number)

# borrar cualquier cosa que no sean dígitos

