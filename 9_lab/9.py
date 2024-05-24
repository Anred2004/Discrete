import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict


edges = [[14, 3], [4, 15], [10, 13], [4, 12], [16, 6], [9, 4],
         [10, 2], [8, 9], [8, 2], [11, 10], [4, 16], [9, 3], [16, 8],
         [15, 3], [11, 4], [13, 5], [5, 7], [12, 8], [5, 14], [5, 2],
         [9, 5], [8, 11], [6, 14], [14, 10], [10, 15], [9, 10], [7, 4],
         [3, 7], [5, 12], [8, 15]]

# Форд-Фалкерсон
class Graph:
    def __init__(self, edges):
        self.graph = defaultdict(list)
        self.matched = {}
        self.construct_graph(edges)

    def construct_graph(self, edges):
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
            self.matched[u] = None
            self.matched[v] = None

    def augmenting_path(self, u, visited):
        if u in visited:
            return False
        visited.add(u)
        for v in self.graph[u]:
            if self.matched[v] is None or self.augmenting_path(self.matched[v], visited):
                self.matched[u] = v
                self.matched[v] = u
                return True
        return False

    def max_matching(self):
        matchings = 0
        for u in self.graph:
            if self.matched[u] is None:
                if self.augmenting_path(u, set()):
                    matchings += 1
        matching_edges = [(u, v) for u, v in self.matched.items() if v is not None]
        for (u, v) in matching_edges:
            if (v,u) in matching_edges:
                matching_edges.remove((v,u))
        return matchings, matching_edges

# Алгоритм Куна
class GraphK:
    def __init__(self, edges):
        self.graph = {}
        self.visited = set()
        self.matched = {}
        self.construct_graph(edges)

    def construct_graph(self, edges):
        for u, v in edges:
            if u not in self.graph:
                self.graph[u] = []
            if v not in self.graph:
                self.graph[v] = []
            self.graph[u].append(v)
            self.matched[u] = None
            self.matched[v] = None

    def dfs(self, u):
        if u in self.visited:
            return False
        self.visited.add(u)
        for v in self.graph[u]:
            if self.matched[v] is None or self.dfs(self.matched[v]):
                self.matched[u] = v
                self.matched[v] = u
                return True
        return False

    def max_matching(self):
        matchings = 0
        for u in self.graph:
            if self.matched[u] is None:
                self.visited = set()
                if self.dfs(u):
                    matchings += 1
        matching_edges = [(u, v) for u, v in self.matched.items() if v is not None]
        for (u, v) in matching_edges:
            if (v,u) in matching_edges:
                matching_edges.remove((v,u))
        return matchings, matching_edges

def is_bipartite(edges):
    graph = {}
    for edge in edges:
        u, v = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    colors = {}
    queue = [next(iter(graph))]
    colors[next(iter(graph))] = 0

    while queue:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if neighbor not in colors:
                colors[neighbor] = 1 - colors[current]
                queue.append(neighbor)
            elif colors[neighbor] == colors[current]:
                return False
    return True

def visualize_graph(edges):
    graph = nx.Graph(edges)
    pos = nx.spring_layout(graph)  # Layout for graph visualization
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    plt.show()



bipartite = is_bipartite(edges)
print("двудольный?", bipartite)

print("алгоритм Форд-Фалкерсона")
g0 = Graph(edges)

# Поиск максимального паросочетания
max_matching0, matching_edges0 = g0.max_matching()

# Вывод результатов
print("Число максимального паросочетания:", max_matching0)
print("Рёбра входящие в максимальное паросочетание:")
for edge in matching_edges0:
    print(edge)

print("Алгоритм Куна")
g = GraphK(edges)

# Поиск максимального паросочетания
max_matching, matching_edges = g.max_matching()

# Вывод результатов
print("Число максимального паросочетания:", max_matching)
print("Рёбра входящие в максимальное паросочетание:")
for edge in matching_edges:
    print(edge)
visualize_graph(edges)
