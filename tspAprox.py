import time

def tspAprox(matrix):

    visited = [False] * len(matrix)
    min_path = 0
    min_weight = 999999
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_weight and not visited[j] and i != j:
                min_weight = matrix[i][j]
                selected_vertex = j      
    
    
    visited[selected_vertex] = True

   # print(min_weight, selected_vertex)
    first_vertex = selected_vertex

    while(visited.count(False) != 0):
        
        min_weight = 999999
        for i in range(len(matrix[i])):
            if matrix[i][selected_vertex] < min_weight and not visited[i] and selected_vertex != i:
                min_weight = matrix[i][selected_vertex]
                selected_vertex_i = i
                selected_vertex_j = selected_vertex
            
        selected_vertex = selected_vertex_i
        visited[selected_vertex] = True
        min_path += min_weight

    min_path += matrix[selected_vertex][first_vertex]
    print(min_path)


matrix = []

with open("tsp1_253.txt", "r") as file:
    for line in file:
        row = line.strip().split()
        matrix.append(row)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = int(matrix[i][j])


start = time.time()
tspAprox(matrix)
end_time = time.time() - start
print(f"Runtime: {end_time} seconds")