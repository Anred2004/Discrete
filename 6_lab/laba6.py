import numpy as np
# список ребер
edges = [
    (0, 1, 11),
    (0, 6, 13),
    (1, 0, 19),
    (1, 3, 15),
    (1, 4, 14),
    (2, 1, 19),
    (2, 7, 18),
    (3, 0, 12),
    (3, 1, 16),
    (3, 5, 14),
    (4, 0, 14),
    (4, 3, 18),
    (4, 6, 14),
    (5, 0, 14),
    (5, 2, 17),
    (5, 4, 19),
    (6, 0, 19),
    (7, 5, 17)
]
# Создаем матрицу смежности
num_vertices = 8
# Создаем нулевую матрицу с размером num_vertices x num_vertices
adj_matrix = np.zeros((num_vertices, num_vertices))

# Заполняем матрицу смежности значениями из списка рёбер
for edge in edges:
    adj_matrix[edge[0]][edge[1]] = edge[2]
print("Матрица смежности:")
print(adj_matrix)

# Перевод матрицы смежности в матрицу инцидентности
def adjacency_to_incidence(adj_matrix):
    num_vertices = len(adj_matrix)
    edges = []

# перебираем все вершины графа
    for i in range(num_vertices):
        for j in range(i+1, num_vertices):
# Проверяем, существует ли ребро между вершинами i и j в матрице смежности
            if adj_matrix[i][j] != 0:
                edges.append((i, j, adj_matrix[i][j]))
# Определяем количество рёбер в графе.
    num_edges = len(edges)
    inc_matrix = np.zeros((num_vertices, num_edges))
# Перебираем список рёбер
    for idx, edge in enumerate(edges):
        inc_matrix[edge[0]][idx] = 1
        inc_matrix[edge[1]][idx] = -1

    return inc_matrix

inc_matrix = adjacency_to_incidence(adj_matrix)

print("\nМатрица инцидентности из матрицы смежности:")
print(inc_matrix)

# Проверяем, является ли граф эйлеровым
# вычисляем степени вершин
degree_sequence = np.sum(adj_matrix, axis=0)
# проверяем степени вершин на четность
is_eulerian = all(degree % 2 == 0 for degree in degree_sequence)

if is_eulerian:
    print("\nГраф является эйлеровым.")
else:
    print("\nГраф не является эйлеровым.")

# Находим кратчайшие пути между всеми вершинами по алгоритму Флойда-Уоршелла
shortest_paths = np.zeros((num_vertices, num_vertices))

for i in range(num_vertices):
    for j in range(num_vertices):
        if i != j:
            shortest_paths[i][j] = np.inf

for edge in edges:
    shortest_paths[edge[0]][edge[1]] = edge[2]

for k in range(num_vertices):
    for i in range(num_vertices):
        for j in range(num_vertices):
            if shortest_paths[i][j] > shortest_paths[i][k] + shortest_paths[k][j]:
                shortest_paths[i][j] = shortest_paths[i][k] + shortest_paths[k][j]

# Вывод кратчайших путей
print("\nКратчайшие пути между всеми вершинами:")
print(shortest_paths)
