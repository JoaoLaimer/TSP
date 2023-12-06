from sys import maxsize
from itertools import permutations
import time

def tsp(graph, s = 0): 
 
    vertex = [] 
    for i in range(len(graph)): 
        if i != s: 
            vertex.append(i) 
    
    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize 
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
        # store current Path weight(cost) 
        current_pathweight = 0
 
        # compute current path weight 
        k = s 
        #print("start")
        for j in i: 
            current_pathweight += graph[k][j] 
            #print(k,j,graph[k][j])
            k = j 

        current_pathweight += graph[k][s] 
        #print(k,s,graph[k][s])
        # update minimum 
        min_path = min(min_path, current_pathweight) 
        
    
    return min_path 

matrix = []

with open("arquivos tsp\\tsp1_253.txt", "r") as file:
    for line in file:
        row = line.strip().split()
        matrix.append(row)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = int(matrix[i][j])

start = time.time()
print(tsp(matrix))
end_time = time.time() - start

print(f"Runtime: {end_time} seconds")
