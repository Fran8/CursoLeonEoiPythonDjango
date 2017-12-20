
ALUMNO = {
    'nombre': 'David',
    'edad': 21,
    'clase': 'python'
}

print(ALUMNO['nombre'])
print(ALUMNO['edad'])
print(ALUMNO['clase'])

print(ALUMNO)

ALUMNO['sexo'] = 'masculino'
print(ALUMNO)

del ALUMNO['sexo']
print(ALUMNO)

del ALUMNO
print(ALUMNO)