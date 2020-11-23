import numpy as np
import networkx as nx
from networkx.algorithms.flow import maximum_flow
import re


class NeuralTriGraphCentralVert():
    def __init__(self,edge):
        self.key = max(edge)
        self.l_edges = []
        self.r_edges = []
        self.l_edges.append(min(edge))

    def add(self,edge):
        mi, mx = min(edge), max(edge)
        if mi == self.key:
            self.r_edges.append(mx)
        elif mx == self.key:
            self.l_edges.append(mi)

    def edge_counts(self):
        l_size = len(self.l_edges)
        r_size = len(self.r_edges)
        self.l_counts = np.ones(l_size)
        self.r_counts = np.ones(r_size)
        if l_size>r_size:
            self.r_counts = distr_evenly(l_size,r_size)
        elif l_size<r_size:
            self.l_counts = distr_evenly(r_size,l_size)


def distr_evenly(n,l):
    ceil=np.ceil(n/l)
    flr=ceil-1
    h=int(n-l*flr)
    j=int(l*ceil-n)
    h_arr = np.ones(h)*ceil
    j_arr = np.ones(j)*flr
    return np.concatenate((h_arr,j_arr))


def create_central_vert_dict(edges1,edges2):
    vert_set = {}
    for e in edges1:
        if e[1] not in vert_set:
            tg = NeuralTriGraphCentralVert(e)
            vert_set[e[1]] = tg
        else:
            vert_set[e[1]].add(e)
    for e in edges2:
        if e[0] not in vert_set:
            tg = NeuralTriGraphCentralVert(e)
            vert_set[e[0]] = tg
        else:
            vert_set[e[0]].add(e)
    return vert_set


class NeuralTriGraph():
    """
    A neural tri-grpah is a special case of a tri-partite
    graph. In it, the vertices can be segregated into three
    layers. However unlike a tri-partite graph, connections
    exist only between successive layers (1 and 2; 2 and 3).
    Such graphs describe the layers of a neural network; 
    hence the name.
    """
    def __init__(self, left_edges, right_edges):
        self.left_edges = left_edges
        self.right_edges = right_edges
        self.vertices = set(left_edges.flatten())\
                    .union(set(right_edges.flatten()))
        self.layer_1 = set(left_edges[:,0])
        self.layer_2 = set(left_edges[:,1])
        self.layer_3 = set(right_edges[:,1])
        self.central_vert_dict = create_central_vert_dict(left_edges,\
                                                        right_edges)

    def create_bipartite_graph(self):
        self.flow_graph = nx.DiGraph()
        for ed in self.left_edges:
            ## The vertices from which flow travels only out.
            v1 = "out_layer0_elem" + str(ed[0])
            v2 = "in_layer1_elem" + str(ed[1])
            self.flow_graph.add_edge(v1,v2,capacity=1,weight=1)
        for ed in self.right_edges:
            v1 = "out_layer1_elem" + str(ed[0])
            v2 = "in_layer2_elem" + str(ed[1])
            self.flow_graph.add_edge(v1,v2,capacity=1,weight=1)
        for k in self.central_vert_dict.keys():
            for l in self.central_vert_dict[k].l_edges:
                for r in self.central_vert_dict[k].r_edges:
                    v1 = "out_layer0_elem" + str(l)
                    v2 = "in_layer2_elem" + str(r)
                    self.flow_graph.add_edge(v1,v2,capacity=1,weight=1)
        v1="source"
        for e in self.layer_1:
            v2 = "out_layer0_elem" + str(e)
            self.flow_graph.add_edge(v1,v2,capacity=1,weight=1)
        for e in self.layer_2:
            v2 = "out_layer1_elem" + str(e)
            self.flow_graph.add_edge(v1,v2,capacity=1,weight=1)
        for e in self.layer_3:
            v2 = "out_layer2_elem" + str(e)
            self.flow_graph.add_edge(v1,v2,capacity=1,weight=1)
        v2="sink"
        for e in self.layer_1:
            v1 = "in_layer0_elem" + str(e)
            self.flow_graph.add_edge(v1,v2,capacity=1,weight=1)
        for e in self.layer_2:
            v1 = "in_layer1_elem" + str(e)
            self.flow_graph.add_edge(v1,v2,capacity=1,weight=1)
        for e in self.layer_3:
            v1 = "in_layer2_elem" + str(e)
            self.flow_graph.add_edge(v1,v2,capacity=1,weight=1)


def tst():
    ## Test case-1
    edges1 = np.array([[1,4],[2,4],[2,5],[3,5]])
    edges2 = np.array([[4,6],[4,7],[5,8]])

    nu = NeuralTriGraph(edges1,edges2)
    nu.create_bipartite_graph()

    ##For debugging:
    [e for e in nu.flow_graph.edges]

    flow_val, flow_dict = nx.maximum_flow(nu.flow_graph, 'source', 'sink')

    ## Test case-2
    edges1 = np.array([[1,5],[2,5],[3,7],[4,6]])
    edges2 = np.array([[5,8],[5,9],[5,10],[7,11],[6,11]])

