import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(range(26))

for i in range(25):
    G.add_edge(i, i + 1)

for i in range(10, 16):
    for j in range(i + 1, 16):
        G.add_edge(i, j)

cent = nx.eigenvector_centrality(G)
values = [cent[i] for i in range(26)]

plt.plot(values, marker='o')
plt.show()
