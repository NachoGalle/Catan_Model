import networkx as nx
import matplotlib.pyplot as plt
from clase_estados import estado, estado_valido, costo
import pickle

G = nx.DiGraph()
s0 = estado()

capas = []*9

def construir_grafo(G: nx.DiGraph,s:estado):
    Q = list()
    dad= None
    Q.append(s)
    while len(Q) > 0:
        dad = Q.pop(0)
        G.add_node(dad, layer = dad.ptos_totales)
        if dad.ptos_totales < 10:
            p_hijo = estado(poblados=dad.poblados+1,ciudades=dad.ciudades,caballeros=dad.caballeros,
                            ruta_larga=dad.ruta_larga,ejercito=dad.ejercito,ptos_victoria=dad.ptos_victoria)
            if estado_valido(p_hijo):
                G.add_node(p_hijo,layer= p_hijo.ptos_totales)
                G.add_edge(dad,p_hijo,costo=costo(dad,p_hijo))
                if p_hijo not in Q:
                    Q.append(p_hijo)
            
            c_hijo = estado(poblados=dad.poblados-1,ciudades=dad.ciudades+1,caballeros=dad.caballeros,
                            ruta_larga=dad.ruta_larga,ejercito=dad.ejercito,ptos_victoria=dad.ptos_victoria)
            if estado_valido(c_hijo):
                G.add_node(c_hijo,layer= c_hijo.ptos_totales)
                G.add_edge(dad,c_hijo,costo=costo(dad,c_hijo))
                if c_hijo not in Q:
                    Q.append(c_hijo)
            
            v_hijo = estado(poblados=dad.poblados,ciudades=dad.ciudades,caballeros=dad.caballeros,
                            ruta_larga=dad.ruta_larga,ejercito=dad.ejercito,ptos_victoria=dad.ptos_victoria+1)
            if estado_valido(v_hijo):
                G.add_node(v_hijo,layer= v_hijo.ptos_totales)
                G.add_edge(dad,v_hijo,costo=costo(dad,v_hijo))
                if v_hijo not in Q:
                    Q.append(v_hijo)
            
            l_hijo = estado(poblados=dad.poblados,ciudades=dad.ciudades,caballeros=dad.caballeros,
                            ruta_larga=dad.ruta_larga+1,ejercito=dad.ejercito,ptos_victoria=dad.ptos_victoria)
            if estado_valido(l_hijo):
                G.add_node(l_hijo,layer= l_hijo.ptos_totales)
                G.add_edge(dad,l_hijo,costo=costo(dad,l_hijo))
                if l_hijo not in Q:
                    Q.append(l_hijo)
            
            e_hijo = estado(poblados=dad.poblados,ciudades=dad.ciudades,caballeros=dad.caballeros,
                            ruta_larga=dad.ruta_larga,ejercito=dad.ejercito+1,ptos_victoria=dad.ptos_victoria)
            if estado_valido(e_hijo):
                G.add_node(e_hijo,layer= e_hijo.ptos_totales)
                G.add_edge(dad,e_hijo,costo=costo(dad,e_hijo))
                if e_hijo not in Q:
                    Q.append(e_hijo)


construir_grafo(G,s0)

pos = nx.multipartite_layout(G, subset_key="layer",align="horizontal")
nx.draw(G, pos, node_color="skyblue")
plt.show()


# save graph object to file
pickle.dump(G, open('grafo_de_estados.pickle', 'wb'))

# load graph object from file
G = pickle.load(open('grafo_de_estados.pickle', 'rb'))

