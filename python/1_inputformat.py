"""
ejemplo para pedir input de usuario y formatear la respuesta
"""
PREGUNTA = '¿Cómo te llamas?'
RESPUESTA = input(PREGUNTA)

print('hola', RESPUESTA, '¿como estas?')

respuesta_formateada = 'hola (),¿como estas?'.format(RESPUESTA)
print(respuesta_formateada)
