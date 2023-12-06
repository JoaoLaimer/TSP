import view as VW
import christofides as CF
import tsp
import tree
import time

path = ["arquivos tsp\\tsp1_253.txt", "arquivos tsp\\tsp2_1248.txt", "arquivos tsp\\tsp3_1194.txt", "arquivos tsp\\tsp4_7013.txt", "arquivos tsp\\tsp5_27603.txt"]

def read_file(path):
    matrix = []
    with open(path, "r") as file:
        for line in file:
            row = line.strip().split()
            matrix.append(row)
    return matrix

if __name__ == "__main__":
    matrix = read_file(path[1])
    CF.find_eulerian_tour(matrix)