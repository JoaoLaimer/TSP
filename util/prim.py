def prim(adj_matrix):
    n = len(adj_matrix)

    visited = [False] * n
    visited[0] = True
    adj = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(n-1):
        min_weight = 999999
        min_vertex = 0
        for j in range(n):
            if visited[j]:
                for k in range(n):
                    if not visited[k] and adj_matrix[j][k] < min_weight:
                        if adj_matrix[j][k] == 0:
                            adj_matrix[j][k] = 1
                        min_weight = adj_matrix[j][k]
                        min_vertex = k
                        source_vertex = j
        visited[min_vertex] = True
        adj[source_vertex][min_vertex] = min_weight
        adj[min_vertex][source_vertex] = min_weight

    return adj
