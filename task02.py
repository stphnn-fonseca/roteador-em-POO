import networkx as nx
import matplotlib.pyplot as plt

# Cria um objeto de grafo vazio
G = nx.Graph()

# Adiciona nós ao grafo
G.add_nodes_from(range(1, 6))

# Adiciona as arestas que formam a topologia de anel
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(5, 1)

# Desenha a topologia
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()