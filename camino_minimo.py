import networkx as nx
import matplotlib.pyplot as plt
from clase_estados import estado
import pickle

with open('grafo_de_estados.pickle', 'rb') as f:
    G = pickle.load(f)

pos = nx.multipartite_layout(G, subset_key="layer",align="horizontal")
nx.draw(G, pos, node_color="skyblue")
plt.show()