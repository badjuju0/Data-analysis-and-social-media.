import networkx as nx
from matplotlib import pyplot as plt

p = 0.55
n = 37

graph = nx.erdos_renyi_graph(n, p)
sum_deg = 0

for n in graph.nodes():
    sum_deg += graph.degree(n)

formula_avg_degree = (n - 1) * p
actual_avg_degree = sum_deg / len(graph.nodes())

difference = formula_avg_degree - actual_avg_degree

print("Фактическое значение :", round(actual_avg_degree, 2))
print("Значение по формуле:", round(formula_avg_degree, 2))
print("Разница:", round(difference, 2))

nx.draw(graph, with_labels=True)
plt.show()
