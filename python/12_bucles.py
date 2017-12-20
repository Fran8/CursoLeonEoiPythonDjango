def print_everything(*args):
    for n in args:
        print(n)

print_everything('manzana', 'platano','pera')

def print__all_with_positions(*args):
    for count, thing in enumerate(args):
        print(count,thing)
print__all_with_positions('manzana', 'platano','pera')

counter = 0
"""while True:
    counter +=1
    print(counter)
    if counter >10098:
        break
print('fin del while')
"""
def count_until(n=3):
    pass

def count_until(n=30):
    counter = 0
    while counter <n:
        counter +=1
        print(counter)

count_until(5)
