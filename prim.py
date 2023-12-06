from tree import Tree

def prim(adj_matrix):
    n = len(adj_matrix)
    mst = Tree(0,adj_matrix[0][0])
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
        #mst.insert_in_tree(source_vertex,Tree(str(min_vertex),min_weight))
        adj[source_vertex][min_vertex] = min_weight
        adj[min_vertex][source_vertex] = min_weight
        #mst.set_odds_in_tree()

    return mst, min_vertex, adj
