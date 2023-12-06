import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
pos_list = [nx.circular_layout, nx.random_layout, nx.shell_layout, nx.spectral_layout, nx.spring_layout, nx.fruchterman_reingold_layout]

def mst_edges(mst):
    edges = []
    for child in mst.children:
        edges.append((int(mst.name),int(child.name)))
        edges.extend(mst_edges(child))
    return edges

def create_view(matrix=None, mst=None, tsp=None, hielholzer=None):

    if matrix is None and mst is None and tsp is None  and hielholzer is None:
        return
    
    num_parameter = Counter([matrix is not None, mst is not None, tsp is not None, hielholzer is not None])[True]

    fig, axs = plt.subplots(1, num_parameter, figsize=(14,7))

    if matrix:
        G = nx.Graph()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    G.add_edge(i,j,weight=matrix[i][j])
                        
        pos = pos_list[2](G) 
        nx.draw(G, pos, with_labels=True, 
                node_size=700, 
                node_color = "skyblue",
                font_size=10, 
                font_color="black", 
                font_weight="bold",
                alpha = 0.7, 
                node_shape="o", 
                edge_color='gray', 
                width=1.0,
                ax=axs[0])
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, 
                                    edge_labels=labels, 
                                    label_pos=0.4, 
                                    font_size=8,
                                    bbox=dict(facecolor='none', edgecolor='none'),
                                    ax=axs[0])
        axs[0].set_title('GRAFO')
        
    if mst:
        MSTG = nx.Graph()
        mst_edges_list = mst_edges(mst)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0 and (i,j) in mst_edges_list :
                    MSTG.add_edge(i,j,weight=matrix[i][j])
        #pos_mst = pos_list[0](MSTG)
        nx.draw(MSTG, pos, with_labels=True,
                node_size=700, 
                node_color = "skyblue",
                font_size=10, 
                font_color="black", 
                font_weight="bold",
                alpha = 0.7, 
                node_shape="o", 
                edge_color='gray', 
                width=1.0,
                ax=axs[1])

        labels_mst = nx.get_edge_attributes(MSTG, 'weight')
        nx.draw_networkx_edge_labels(MSTG, pos,
                                    edge_labels=labels_mst,
                                    label_pos=0.4,
                                    font_size=8,
                                    bbox=dict(facecolor='none', edgecolor='none'),
                                    ax=axs[1]) 
        axs[1].set_title('MST')

    if tsp:
        TSP = nx.Graph()
        for i in range(len(tsp)):
            TSP.add_edge(tsp[i][0], tsp[i][1], weight=tsp[i][2])
        #pos_tsp = pos_list[0](TSP)
        nx.draw(TSP, pos, with_labels=True,
                node_size=700, 
                node_color = "skyblue",
                font_size=10, 
                font_color="black", 
                font_weight="bold",
                alpha = 0.7, 
                node_shape="o", 
                edge_color='gray', 
                width=1.0,
                ax=axs[2])

        labels_tsp = nx.get_edge_attributes(TSP, 'weight')
        nx.draw_networkx_edge_labels(TSP, pos,
                                    edge_labels=labels_tsp,
                                    label_pos=0.4,
                                    font_size=8,
                                    bbox=dict(facecolor='none', edgecolor='none'),
                                    ax=axs[2]) 
        axs[2].set_title('TSP')
    """
    if unify_matrix:
        T = nx.Graph()
        for i in range(len(unify_matrix)):
            for j in range(len(unify_matrix[i])):
                if unify_matrix[i][j] != 0:
                    T.add_edge(i,j,weight=unify_matrix[i][j])
        #pos = pos_list[2](T) 
        nx.draw(T, pos, with_labels=True, 
                node_size=700, 
                node_color = "skyblue",
                font_size=10, 
                font_color="black", 
                font_weight="bold",
                alpha = 0.7, 
                node_shape="o", 
                edge_color='gray', 
                width=1.0,
                ax=axs[3])
        labels = nx.get_edge_attributes(T, 'weight')
        nx.draw_networkx_edge_labels(T, pos, 
                                    edge_labels=labels, 
                                    label_pos=0.4, 
                                    font_size=8,
                                    bbox=dict(facecolor='none', edgecolor='none'),
                                    ax=axs[3])
        axs[3].set_title('UNIFY MATRIX')
    """
    if hielholzer:
        H = nx.Graph()
        for i in range(len(hielholzer)):
            if i+1 < len(hielholzer):
                H.add_edge(hielholzer[i], hielholzer[i+1])

        nx.draw(H, pos, with_labels=True, 
                node_size=700, 
                node_color = "skyblue",
                font_size=10, 
                font_color="black", 
                font_weight="bold",
                alpha = 0.7, 
                node_shape="o", 
                edge_color='gray', 
                width=1.0,
                ax=axs[3])
        
        axs[3].set_title('EULETIAN TOUR')
    plt.show()
def create_view_test(matrix=None, mst=None, hielholzer=None, test=None):

    if matrix is None and mst is None and hielholzer is None and test is None:
        return
    
    num_parameter = Counter([matrix is not None, mst is not None, hielholzer is not None, test is not None])[True]

    fig, axs = plt.subplots(1, num_parameter, figsize=(14,7))

    if matrix:
        G = nx.Graph()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    G.add_edge(i,j,weight=matrix[i][j])
                        
        pos = pos_list[2](G) 
        nx.draw(G, pos, with_labels=True, 
                node_size=700, 
                node_color = "skyblue",
                font_size=10, 
                font_color="black", 
                font_weight="bold",
                alpha = 0.7, 
                node_shape="o", 
                edge_color='gray', 
                width=1.0,
                ax=axs[0])
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, 
                                    edge_labels=labels, 
                                    label_pos=0.4, 
                                    font_size=8,
                                    bbox=dict(facecolor='none', edgecolor='none'),
                                    ax=axs[0])
        axs[0].set_title('GRAFO')
        
    if mst:
        MSTG = nx.Graph()
        mst_edges_list = mst_edges(mst)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0 and (i,j) in mst_edges_list :
                    MSTG.add_edge(i,j,weight=matrix[i][j])
        #pos_mst = pos_list[0](MSTG)
        nx.draw(MSTG, pos, with_labels=True,
                node_size=700, 
                node_color = "skyblue",
                font_size=10, 
                font_color="black", 
                font_weight="bold",
                alpha = 0.7, 
                node_shape="o", 
                edge_color='gray', 
                width=1.0,
                ax=axs[1])

        labels_mst = nx.get_edge_attributes(MSTG, 'weight')
        nx.draw_networkx_edge_labels(MSTG, pos,
                                    edge_labels=labels_mst,
                                    label_pos=0.4,
                                    font_size=8,
                                    bbox=dict(facecolor='none', edgecolor='none'),
                                    ax=axs[1]) 
        axs[1].set_title('MST')

    if hielholzer:
        H = nx.Graph()
        for i in range(len(hielholzer)):
            if i+1 < len(hielholzer):
                H.add_edge(hielholzer[i], hielholzer[i+1])

        nx.draw(H, pos, with_labels=True, 
                node_size=700, 
                node_color = "skyblue",
                font_size=10, 
                font_color="black", 
                font_weight="bold",
                alpha = 0.7, 
                node_shape="o", 
                edge_color='gray', 
                width=1.0,
                ax=axs[2])
        
        axs[2].set_title('EULETIAN TOUR')

    if test:
        T = nx.Graph()
        for i in range(len(test)):
            for j in range(len(test[i])):
                if test[i][j] != 0:
                    T.add_edge(i,j,weight=test[i][j])
        #pos_tsp = pos_list[0](TSP)
        nx.draw(T, pos, with_labels=True,
                node_size=700, 
                node_color = "skyblue",
                font_size=10, 
                font_color="black", 
                font_weight="bold",
                alpha = 0.7, 
                node_shape="o", 
                edge_color='gray', 
                width=1.0,
                ax=axs[3])

        labels_tsp = nx.get_edge_attributes(T, 'weight')
        nx.draw_networkx_edge_labels(T, pos,
                                    edge_labels=labels_tsp,
                                    label_pos=0.4,
                                    font_size=8,
                                    bbox=dict(facecolor='none', edgecolor='none'),
                                    ax=axs[3]) 
        axs[3].set_title('Test')
    plt.show()

def create_final_view(test=None):
    if test:
        #print(test)
        T = nx.Graph()
        for i in range(len(test)):
            for j in range(len(test[i])):
                if test[i][j] != 0:
                    T.add_edge(i,j)
        pos = pos_list[2](T) 
        nx.draw(T, pos, with_labels=True,
                node_size=700, 
                node_color = "skyblue",
                font_size=10, 
                font_color="black", 
                font_weight="bold",
                alpha = 0.7, 
                node_shape="o", 
                edge_color='gray', 
                width=1.0,)

        labels_tsp = nx.get_edge_attributes(T, 'weight')
        nx.draw_networkx_edge_labels(T, pos,
                                    edge_labels=labels_tsp,
                                    label_pos=0.4,
                                    font_size=8,
                                    bbox=dict(facecolor='none', edgecolor='none'),) 
    plt.show()
"""
if __name__ == '__main__':
    matrix = read_matrix()
    print_matrix(matrix)
    create_view(matrix)
"""    
    
    