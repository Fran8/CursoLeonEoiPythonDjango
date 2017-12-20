from libs.urlloader import load_url
from urllib.error import HTTPError

try:
    raise Exception('esto no funciona nunca')
    print('funcionará??')    
except Exception as eror: 
    print('ha fallado:', repr(error))

try:
    load_url('http://noexiste.commm')
except HTTPError as error:
    print('Error al cargar la url:', repr(error))
except Exception as ex:
    print('Error genérico:', repr(ex))
