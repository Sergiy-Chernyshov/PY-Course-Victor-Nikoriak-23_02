#Task1

def dfs_fill_order(v, graph, visited, stack):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs_fill_order(neighbor, graph, visited, stack)
    stack.append(v)


def dfs_collect_component(v, rev_graph, visited, component):
    visited[v] = True
    component.append(v)
    for neighbor in rev_graph[v]:
        if not visited[neighbor]:
            dfs_collect_component(neighbor, rev_graph, visited, component)


def reverse_graph(graph):
    n = len(graph)
    rev = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            rev[v].append(u)
    return rev


def strongly_connected_components(graph):
    n = len(graph)
    visited = [False] * n
    stack = []

    for v in range(n):
        if not visited[v]:
            dfs_fill_order(v, graph, visited, stack)

    rev_graph = reverse_graph(graph)

    visited = [False] * n
    scc_list = []

    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs_collect_component(v, rev_graph, visited, component)
            scc_list.append(component)

    return scc_list



graph = [
    [1],        # 0 -> 1
    [2, 4, 5],  # 1 -> 2,4,5
    [3, 6],     # 2 -> 3,6
    [2, 7],     # 3 -> 2,7
    [0, 5],     # 4 -> 0,5
    [6],        # 5 -> 6
    [5],        # 6 -> 5
    [3, 6]      # 7 -> 3,6
]

scc = strongly_connected_components(graph)

print("Сильно зв'язні компоненти (SCC):")
for i, comp in enumerate(scc, start=1):
    print(f"Компонента {i}: {comp}")

print("\n")

#Task2

from collections import deque

def bfs_shortest_paths_from_source(graph, start):

    n = len(graph)
    dist = [-1] * n
    parent = [-1] * n

    queue = deque()
    queue.append(start)
    dist[start] = 0

    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[v] + 1
                parent[neighbor] = v
                queue.append(neighbor)

    return dist, parent


def all_pairs_shortest_paths_bfs(graph):

    n = len(graph)
    all_dist = []
    all_parent = []

    for s in range(n):
        dist, parent = bfs_shortest_paths_from_source(graph, s)
        all_dist.append(dist)
        all_parent.append(parent)

    return all_dist, all_parent


def restore_path(parent, start, end):
    if start == end:
        return [start]
    if parent[end] == -1:
        return []  # шляху немає

    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        if cur == start:
            break
        cur = parent[cur]

    path.reverse()
    if path[0] != start:
        return []
    return path

graph = [
    [1, 3],       # 0
    [0, 2, 4],    # 1
    [1, 5],       # 2
    [0, 4],       # 3
    [1, 3, 5],    # 4
    [2, 4]        # 5
]

all_dist, all_parent = all_pairs_shortest_paths_bfs(graph)

print("Матриця найкоротших відстаней:")
for i, row in enumerate(all_dist):
    print(f"Від вершини {i}: {row}")

start, end = 0, 5
path = restore_path(all_parent[start], start, end)
if path:
    print(f"\nНайкоротший шлях {start} -> {end}: {path}")
    print(f"Довжина шляху: {all_dist[start][end]}")
else:
    print(f"\nШляху {start} -> {end} немає")