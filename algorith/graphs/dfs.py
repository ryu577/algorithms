import numpy as np

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

## Recursive version of depth first search.
def dfs_r(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_r(graph, next, visited)
    return visited


class Tests():
    ## https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
    @staticmethod
    def tst():
        graph = {'A': set(['B', 'C']),
                'B': set(['A', 'D', 'E']),
                'C': set(['A', 'F']),
                'D': set(['B']),
                'E': set(['B', 'F']),
                'F': set(['C', 'E'])}
        dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}

