import time
seconds = time.time()
print('numero de ticks desde las 12 del 1 de enero 19')

# hora local
local_time = time.localtime(seconds)
print(local_time)
print(type(local_time))

#hora formateada
asctime = time.asctime(local_time)
print(asctime)

# hora con formato personalizado
date_format = ''
date_formatted = time.strftime(date_format, time.gmtime(seconds))
print(date_formatted)
