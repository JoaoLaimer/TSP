from scipy.optimize import linear_sum_assignment
path = ["arquivos tsp\\tsp1_253.txt", "arquivos tsp\\tsp2_1248.txt", "arquivos tsp\\tsp3_1194.txt", "arquivos tsp\\tsp4_7013.txt", "arquivos tsp\\tsp5_27603.txt"]

class Tree(object):
    def __init__(self, name='root',weight=0,children=None,parent=None):
        self.name = str(name)
        self.weight = weight
        self.children = []
        self.isOdd = False
        self.parent = parent
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name
    
    def search(self,name):
        if self.name == name:
            return self
        for child in self.children:
            result = child.search(name)
            if result is not None:
                return result
        return None
    
    def add_child(self,node):
        assert isinstance(node,Tree)
        self.children.append(node)
        node.parent = self

    def insert_in_tree(self,name,child):
        node = self.search(str(name))
        if node is not None:
            node.add_child(child)
        else:
            raise ValueError("Node not found")  
        
    def preorder(self,weight):
        weight[0] += self.weight
        for child in self.children:
            child.preorder(weight)
    
    def setOddsInTree(self):
        self.find_odd()
        for child in self.children:
            child.setOddsInTree()
            
    def find_odd(self):
        if len(self.children) % 2 != 0 and self.parent is not None:
            self.isOdd = False
        elif len(self.children) % 2 == 0 and self.parent is not None:
            self.isOdd = True
        elif len(self.children) % 2 != 0 and self.parent is None:
            self.isOdd = True
        else:
            self.isOdd = False

def prims(adj_matrix):
    n = len(adj_matrix)
    mst = Tree(0,adj_matrix[0][0])
    prims = [[0 for _ in range(n)] for _ in range(n)]
    visited = [False] * n
    visited[0] = True

    for _ in range(n-1):
        min_weight = 999999
        min_vertex = 0
        for j in range(n):
            if visited[j]:
                for k in range(n):
                    if not visited[k] and adj_matrix[j][k] < min_weight:
                        min_weight = adj_matrix[j][k]
                        min_vertex = k
                        source_vertex = j
        visited[min_vertex] = True
        mst.insert_in_tree(source_vertex,Tree(str(min_vertex),min_weight))
        prims[source_vertex][min_vertex] = min_weight
        prims[min_vertex][source_vertex] = min_weight

        mst.setOddsInTree()

    return mst, prims

def min_perfect_matching(matrixzeros,matrixinf):
    
    row_ind, col_ind = linear_sum_assignment(matrixinf)

    min_matching = [(i, j) for i, j in zip(row_ind, col_ind) if matrixzeros[i][j] != 0]

    return min_matching

def oddsMatrixes(matrixMst,matrix):
    
    vertex = [False] * len(matrix)

    for i in range(len(matrix)):
        count = 0
        for j in range(len(matrix)):
            if matrixMst[i][j] != 0:
                count += 1
        if(count % 2 != 0):
            vertex[i] = True

    matrixzeros = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if vertex[j] == False or vertex[i] == False:
                matrix[i][j] = 0
            else:
                matrixzeros[i][j] = matrix[i][j]
    

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if vertex[j] == False or vertex[i] == False:
                matrix[i][j] = 99999999999
            if j == i:
                matrix[i][j] = 99999999999
    matrixinf = matrix    

    return matrixzeros, matrixinf

matrix = []

with open(path[3], "r") as file:
    for line in file:
        row = line.strip().split()
        matrix.append(row)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = int(matrix[i][j])

for i in range(len(matrix)):
    print(len(matrix[i]))

print(len(matrix))
        

mst, primsMatrix = prims(matrix)

matrixzeros,matrixinf = oddsMatrixes(primsMatrix,matrix)

min_matching = min_perfect_matching(matrixzeros,matrixinf)

print(min_matching)

total = [0]
mst.preorder(total)

#print(total)


