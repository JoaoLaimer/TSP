class Graph:
    def __init__(self, n, adjacency_matrix):
        self.adjList = [[] for _ in range(n)]
        self.build_graph(adjacency_matrix)

    def build_graph(self, adjacency_matrix):
        for i in range(len(adjacency_matrix)):
            for j in range(len(adjacency_matrix[i])):
                if adjacency_matrix[i][j] == 1:
                    self.addEdge(i, j)

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

def DFS(graph, v, discovered):
    discovered[v] = True
    for u in graph.adjList[v]:
        if not discovered[u]:
            DFS(graph, u, discovered)

def isConnected(graph, n):
    discovered = [False] * n
    for i in range(n):
        if len(graph.adjList[i]):
            DFS(graph, i, discovered)
            break

    for i in range(n):
        if not discovered[i] and len(graph.adjList[i]):
            return False

    return True

def countOddVertices(graph):
    count = 0
    for lst in graph.adjList:
        if len(lst) % 2 != 0:
            count += 1
    return count

if __name__ == '__main__':
    # Adjacency matrix for the graph
    adjacency_matrix = [[0, 64, 378, 0, 0, 0], [64, 0, 0, 0, 0, 164], [378, 0, 0, 170, 0, 0], [0, 0, 170, 0, 223, 0], [0, 0, 0, 223, 0, 273], [0, 164, 0, 0, 273, 0]]

    n = len(adjacency_matrix)
    graph = Graph(n, adjacency_matrix)

    is_connected_graph = isConnected(graph, n)

    odd_vertices_count = countOddVertices(graph)

    if is_connected_graph and (odd_vertices_count == 0 or odd_vertices_count == 2):
        print('The graph has an Eulerian path')

        if odd_vertices_count == 0:
            print('The graph has an Eulerian cycle')
        else:
            print('The Graph is Semi–Eulerian')
    else:
        print('The Graph is not Eulerian')