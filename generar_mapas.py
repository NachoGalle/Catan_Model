import random
import networkx as nx
import matplotlib.pyplot as plt

TERRENOS = ["Arcilla","Arcilla","Arcilla","Madera","Madera","Madera","Madera","Oveja","Oveja","Oveja","Oveja"
            ,"Trigo","Trigo","Trigo","Trigo","Piedra","Piedra","Piedra","Desierto"]

terrenos = TERRENOS.copy()
random.shuffle(terrenos)

NUMEROS = (5,2,6,3,8,10,9,12,11,4,8,10,9,4,5,6,3,11)

class posicion():
    def __init__(self,loc:tuple =None,pob:bool=False,ciud: bool=False,vecinos: dict= None ,recursos: list= None,puerto: list = None):
        self.loc=loc
        self.ocupable=True
        self.poblado= pob
        self.ciudad= ciud
        self.vecinos= vecinos if vecinos is not None else {}
        self.recursos = recursos if recursos is not None else []
        self.puerto = puerto if puerto is not None else [0,0,0,0,0]
        self.atributos = {"loc": loc, "ocupable": self.ocupable, "poblado": pob, "ciudad": ciud , "vecinos" : self.vecinos}

    def add_recurso(self,recurso: tuple):
        self.recursos.append(recurso)

    def __eq__(self, other):
        if not isinstance(other, posicion):
            return False
        return self.loc == other.loc

    def __hash__(self):
        return hash(self.loc)


class tablero():
    def __init__(self):
        self.espacios=          {1:[None,0],12:[None,0],11:[None,0],
                            2:[None,0],13:[None,0],18:[None,0],10:[None,0],
                        3:[None,0],14:[None,0],19:[None,0],17:[None,0],9:[None,0],
                            4:[None,0],15:[None,0],16:[None,0],8:[None,0],
                                5:[None,0],6:[None,0],7:[None,0]}

    def poner_terrenos(self,terrenos= terrenos):
        for i in range(1,20):
            self.espacios[i]=[terrenos[i-1],0]

    def generar_desde(self,n):
        if n > 12:pass
        i=0
        actual = n
        while actual < 20:
            if self.espacios[actual][0] != "Desierto" and self.espacios[actual][1] == 0:
                self.espacios[actual][1] = NUMEROS[i]
                i+=1
                if actual == 12: actual = 1
                elif actual == 18: actual = 13
                else: actual +=1
            elif self.espacios[actual][0] == "Desierto":
                actual+=1
            else:
                if actual == 2 or actual == 3: actual = 14
                elif actual == 4 or actual == 5: actual = 15
                elif actual == 6 or actual == 7: actual = 16
                elif actual == 8 or actual == 9: actual = 17
                elif actual == 10 or actual == 11: actual = 18
                elif actual == 1 or actual == 12: actual = 13
                else: actual = 19
        self._pasar_a_tuplas()

    def generar_random(self):
        n=random.randint(1,12)
        self.generar_desde(n)

    def _pasar_a_tuplas(self):
        for i in range(1,20):
            self.espacios[i]=tuple(self.espacios[i])

def n_prob(n: int) -> float:
    return (6-abs(n-7))/36

def generar_grafo_posiciones(G: nx.Graph):
    for x in range(11):
        for y in range(6):
            if (abs(y-2.5) > 2 and (x < 2 or x > 8)) or (abs(y-2.5) > 1 and (x == 0 or x == 10)):
                continue

            G.add_node((x, y), posicion=posicion(loc=(x, y)),pos=(x, y)) #revisar parámetros de add_node tal vez sea mejor que la posición sea el nodo y no que sea un atributo del nodo#
            if (x-1,y) in G.nodes():
                G.add_edge((x-1,y),(x,y))
            if (x,y-1) in G.nodes() and (x+y)%2 != 0:
                G.add_edge((x,y-1),(x,y))


G=nx.Graph()
generar_grafo_posiciones(G)

def cargar_tablero(G: nx.Graph,Tablero: tablero):
    for i in [(2,0),(3,0),(4,0),(2,1),(3,1),(4,1)]:
        recurso = Tablero.espacios[5]
        G.nodes[i]["posicion"].add_recurso(recurso)


tab = tablero()
tab.poner_terrenos(TERRENOS)
tab.generar_random()

print(tab.espacios)

cargar_tablero(G,tab)
print(len(G.nodes[2,0]["posicion"].recursos))

for i in [(2,0),(3,0),(4,0),(2,1),(3,1),(4,1)]:
    print(str(G.nodes[i]) + "recs" + str(G.nodes[i]["posicion"].recursos))

pos = nx.get_node_attributes(G, "pos")
nx.draw(G, pos=pos, node_color="skyblue")
plt.show()

print(list(G.nodes(data="posicion")))