import numpy as np
from queue import Queue

def generate(n):
    G = []
    for i in range(n):  # Цикл по всем вершинам графа
        deg = np.random.randint(10, 100)  # Генерация случайной степени вершины от 10 до 100
        range1 = np.arange(i)
        range2 = np.arange(i + 1, n)
        all_range = np.union1d(range1, range2)
        G.append(np.random.choice(all_range, deg, replace=False).tolist())

    # Добавляем подграф K4
    if n >= 4:
        k4_vertices = np.random.choice(range(n), 4, replace=False)
        for v in k4_vertices:
            for u in k4_vertices:
                if u != v:
                    G[v].append(u)

    # Добавляем подграф K3
    if n >= 3:
        k3_vertices = np.random.choice(range(n), 3, replace=False)
        for v in k3_vertices:
            for u in k3_vertices:
                if u != v:
                    G[v].append(u)

    cnt = 0  # Инициализация счетчика ребер
    for i in range(len(G)):
        for j in range(len(G[i])):
            cnt += 1
    print("количество ребер", cnt)
    return G

def is_connected(n, G):
    visited = [False] * n

    def dfs(v):
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                dfs(u)

    dfs(0)  # Начинаем обход с произвольной вершины

    if all(visited):
        print("Граф связный")
    else:
        print("Граф несвязный")
        
def is_sparse(n, G):
    num_edges = sum(len(adj_list) for adj_list in G)
    max_edges = n * (n - 1) / 2  # Максимальное количество рёбер в полном графе

    if num_edges < 0.5 * max_edges:
        print("Граф разреженный")
    else:
        print("Граф не разреженный")

# алгоритм поиска в ширину (BFS)
def first(n, G):
    iters = 0
    u = 0  # Начальная вершина
    q = Queue()
    q.put(u)
    dist = [float('inf')] * n  # Инициализация массива расстояний
    dist[u] = 0  # Расстояние от начальной вершины до себя равно 0
    while not q.empty():
        i = q.get()
        iters += 1
        for j in G[i]:
            iters += 1
            if dist[j] == float('inf'):
                dist[j] = dist[i] + 1
                q.put(j)
    print("кратчайшие пути(алгоритм BFS)")
    print(dist)
    print("количество итераций: ", iters)

def second(n, G):
    iters = 0
    u = 0  # Начальная вершина
    dist = [float('inf')] * n
    used = [False] * n
    dist[u] = 0
    for i in range(n):
        v = None
        for j in range(n):
            iters += 1
            if (not used[j]) and (v is None or dist[j] < dist[v]):
                v = j
        if dist[v] == float('inf'):
            break
        used[v] = True
        for e in G[v]:
            iters += 1
            if dist[v] + 1 < dist[e]:
                dist[e] = dist[v] + 1
    print("кратчайшие пути(алгоритм Дейкстры)")
    print(dist)
    print("количество итераций: ", iters)

def main():
    for n in [1200]:
        G = generate(n)
        print('количество вершин:', n)
        first(n, G)
        second(n, G)
main()
