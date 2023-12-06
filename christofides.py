from scipy.optimize import linear_sum_assignment
from util.prim import prim as PRIM
import copy 
import time

def min_perfect_matching(matrixzeros,matrixinf):
    row_ind, col_ind = linear_sum_assignment(matrixinf)
    min_matching = [(i, j) for i, j in zip(row_ind, col_ind) if matrixzeros[i][j] != 0 and i > j]

    matrix_min_matching = [[0 for _ in range(len(matrixinf))] for _ in range(len(matrixinf))]
    
    for i,j in min_matching:
        matrix_min_matching[i][j] = matrixinf[i][j]
        matrix_min_matching[j][i] = matrixinf[j][i]

    return matrix_min_matching

def odds_matrixes(matrixMst,matrix):
    matrix_copy = copy.deepcopy(matrix)
    vertex = [False] * len(matrix_copy)

    for i in range(len(matrix_copy)):
        count = 0
        for j in range(len(matrix_copy)):
            if matrixMst[i][j] != 0:
                count += 1
        if(count % 2 != 0):
            vertex[i] = True

    matrixzeros = [[0 for _ in range(len(matrix_copy))] for _ in range(len(matrix_copy))]

    for i in range(len(matrix_copy)):
        for j in range(len(matrix_copy)):
            if vertex[j] == False or vertex[i] == False:
                matrix_copy[i][j] = 0
            else:
                matrixzeros[i][j] = matrix_copy[i][j]
    
    for i in range(len(matrix_copy)):
        for j in range(len(matrix_copy)):
            if vertex[j] == False or vertex[i] == False:
                matrix_copy[i][j] = 99999999999
            if j == i:
                matrix_copy[i][j] = 99999999999
                
    matrixinf = matrix_copy    

    return matrixzeros, matrixinf      

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()


def transform_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])
    return matrix

def min_matrix(min_matching, matrix):
    min_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]

    for i in range (len(min_matching)):
        min_matrix[min_matching[i][0]][min_matching[i][1]] = matrix[min_matching[i][0]][min_matching[i][1]]
        min_matrix[min_matching[i][1]][min_matching[i][0]] = matrix[min_matching[i][1]][min_matching[i][0]]
    
    return min_matrix

def unify_matrix(min_matrix, matrix):
    result_matrix = [row.copy() for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if min_matrix[i][j] != 0:
                result_matrix[i][j] = min_matrix[i][j]

    return result_matrix

def deep_first_search(matrix, v, visited):
    visited[v] = True
    for i in range(len(matrix[v])):
        if matrix[v][i] != 0 and not visited[i]:
            deep_first_search(matrix, i, visited)

def is_connected(matrix):
    num_vertices = len(matrix)
    visited = [False] * num_vertices

    for i in range(num_vertices):
        if sum(matrix[i]) > 0:
            deep_first_search(matrix, i, visited)
            break

    for i in range(num_vertices):
        if not visited[i] and sum(matrix[i]) > 0:
            return False

    return True

def odd_degree(matrix):
    odd = []
    for i in range(len(matrix)):
        count = 0
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                count += 1
        if(count % 2 != 0):
            odd.append(i)
    return odd

def find_eulerian_tour(matrix):

        matrix = transform_matrix(matrix)
        mst_matrix = PRIM(matrix)
        matrix_zeros, matrix_inf = odds_matrixes(mst_matrix, matrix)
        min_matching = min_perfect_matching(matrix_zeros, matrix_inf)


        T = unify_matrix(min_matching, mst_matrix)
        is_connected_T = is_connected(T)

        if is_connected_T and len(odd_degree(T))%2 == 0:
            
            H, W = hierholzer(T)
            HM = build_matrix(H)
            peso = compare_matrix(matrix, HM)
            print(peso)
        else:
            print("deu ruim")

def compare_matrix(matrix1, matrix2):
    weight = 0
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            if i > j and matrix2[i][j] != 0:
                weight += matrix1[i][j]
    return weight


def hierholzer(matrix, start = 0):
    temp_matrix = copy.deepcopy(matrix)
    vertex = start
    stack =[vertex]
    h_path = []
    h_weight = 0
    while len(stack) != 0:
        vertex = stack[-1]
        if sum(temp_matrix[vertex]) > 0:
            neighbour = [index for index, edge in enumerate(temp_matrix[vertex]) if edge > 0]
            destiny = neighbour[0]
            stack.append(destiny)
            h_weight += temp_matrix[vertex][destiny]
            temp_matrix[vertex][destiny] = 0
            temp_matrix[destiny][vertex] = 0
            vertex = destiny
        else:
            stack.pop()
            h_path.append(vertex)
    return h_path, h_weight

def build_matrix(path):
    vertices = []
    for vertex in path[:-1]:
        if vertex not in vertices:
            vertices.append(vertex)
    vertices.append(path[-1])
    
    if vertices[len(vertices)-1] != vertices[0]:
        vertices.append(vertices[0])
    
    num_vertices = len(vertices) - 1
    new_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        current_vertex = vertices[i]
        next_vertex = vertices[i + 1]
        new_matrix[current_vertex][next_vertex] = 1
        new_matrix[next_vertex][current_vertex] = 1
    
    return new_matrix

def read_file(path):
    matrix = []
    with open(path, "r") as file:
        for line in file:
            row = line.strip().split()
            matrix.append(row)
    return matrix

path = ["arquivos tsp\\tsp1_253.txt", "arquivos tsp\\tsp2_1248.txt", "arquivos tsp\\tsp3_1194.txt", "arquivos tsp\\tsp4_7013.txt", "arquivos tsp\\tsp5_27603.txt"]
if __name__ == "__main__":
    start = time.time()
    matrix = read_file(path[4])
    matrix = transform_matrix(matrix)
    find_eulerian_tour(matrix)

    end_time = time.time() - start

    print(f"Runtime: {end_time} seconds")
