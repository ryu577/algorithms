import networkx as nx
from collections import defaultdict


def create_graph(edges):
    """
    Convert a collection of edges into networkx graph.
    """
    g = nx.Graph()
    for i in edges:
        g.add_edge(i[0],i[1],capacity=np.inf,weight=1)
    return g


def min_edge_cover(edges):
    g=create_graph(edges)
    mc = nx.min_edge_cover(g)
    res = set()
    for i in mc:
        res.add((min(i),max(i)))
    return res


class Node1():
    def __init__(self, key="a", color="white"):
        self.color = color
        self.key = key

    def __hash__(self):
        return self.key


def tst1():
    edges = [[1,2],[1,3],[1,4]]
    g = defaultdict(list)
    for ed in edges:
        vert_0 = Node1(ed[0])
        vert_1 = Node1(ed[1])
        g[vert_0].append(vert_1)

