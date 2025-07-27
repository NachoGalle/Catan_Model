import random

TERRENOS = ["Arcilla","Arcilla","Arcilla","Madera","Madera","Madera","Madera","Oveja","Oveja","Oveja","Oveja"
            ,"Trigo","Trigo","Trigo","Trigo","Piedra","Piedra","Piedra","Desierto"]

NUMEROS = (5,2,6,3,8,10,9,12,11,4,8,10,9,4,5,6,3,11)

class posicion():
    def __init__(self):
        self.pos=None
        self.ocupable=True
        self.poblado= False
        self.ciudad= False
        self.vecinos= {}
        self.recursos = []
        self.puerto = [0,0,0,0,0]

class mapa():
    def __init__(self,terrenos = random.shuffle(TERRENOS)):
        self.terrenos = terrenos
        self.espacios=          {1:[None,0],12:[None,0],11:[None,0],
                            2:[None,0],13:[None,0],18:[None,0],10:[None,0],
                        3:[None,0],14:[None,0],19:[None,0],17:[None,0],9:[None,0],
                            4:[None,0],15:[None,0],16:[None,0],8:[None,0],
                                5:[None,0],6:[None,0],7:[None,0]}
