class Thing:
    pass

thing = Thing()

#constructor sin argumentos o parametros
class Fruit:
    def _init_(self):
        print('objeto fruta')

fruit = Fruit()

# argumentos sin constructor
class CustomFruit:
    """esta clase no vale para mucho pero le gusta poner comentarios"""
    COUNTER = 0

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.juices = 0
        CustomFruit.COUNTER += 1
    
    def __str__(self):
        return 'Soy fruta, me llamo {} y mi color es {}'\
            .format(self.name, self.color)
            
    def make_juice(self, count):
        for n in range(count):
            print('haciendo zumo de ', self.name)
            self.juices += 1
        
custom = CustomFruit('Pera', 'verde')
print(custom)
custom.make_juice(2)

c2 = CustomFruit('Limon', 'amarillo')
print(c2)
c2.make_juice(4)
print('zumos hechos', c2.juices)

