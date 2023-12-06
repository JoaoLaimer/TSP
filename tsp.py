from sys import maxsize
from itertools import permutations
import time

def tsp(graph, start = 0): 
 
    vertice = [] 
    for i in range(len(graph)): 
        if i != start: 
            vertice.append(i) 
    min_path = maxsize 
    next_permutation=permutations(vertice)
    for i in next_permutation:
 
        current_pathweight = 0
        k = start 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 

        current_pathweight += graph[k][start] 
        min_path = min(min_path, current_pathweight) 
        
    
    return min_path 

def read_file(path):
    matrix = []
    with open(path, "r") as file:
        for line in file:
            row = line.strip().split()
            matrix.append(row)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = int(matrix[i][j])

    return matrix

path = ["arquivos tsp\\tsp1_253.txt", "arquivos tsp\\tsp2_1248.txt", "arquivos tsp\\tsp3_1194.txt", "arquivos tsp\\tsp4_7013.txt", "arquivos tsp\\tsp5_27603.txt"]

matrix = read_file(path[1])

start = time.time()
print(tsp(matrix))
end_time = time.time() - start

print(f"Runtime: {end_time} seconds")
