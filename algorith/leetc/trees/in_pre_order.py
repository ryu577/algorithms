import numpy as np
from optimizn.trees.pprnt import display
from optimizn.ab_split.trees.lvlTrees import Node1


def toy_tree1():
    n1 = Node1(3)
    n2 = Node1(9)
    n3 = Node1(20)
    n1.left = n2
    n1.right = n3
    n4 = Node1(15)
    n5 = Node1(7)
    n3.left = n4
    n3.right = n5
    display(n1)
    return n1


def toy_tree2():
    n1 = Node1(3)
    n2 = Node1(9)
    n3 = Node1(20)
    n1.left = n2
    n1.right = n3
    display(n1)
    return n1


class Tree():
    def __init__(self, preorder=[3, 9, 20, 15, 7],
                 inorder=[9, 3, 15, 20, 7]):
        self.preorder = preorder
        self.inorder = inorder
        self.n = len(self.inorder)
        self.ixx = -1

    def findin(self, rix, start, end):
        for i in range(start, end+1):
            if self.inorder[i] == rix:
                return i
        return -1

    def make_tree(self, start=0, end=-2):
        if end < -1:
            end = self.n - 1
        if end < start:
            return None
        self.ixx += 1
        if end == start:
            return Node1(self.inorder[start])
        root_ix = self.preorder[self.ixx]
        fix = self.findin(root_ix, start, end)
        root = Node1(root_ix)
        root.left = self.make_tree(start, fix-1)
        root.right = self.make_tree(fix+1, end)
        return root


if __name__ == "__main__":
    t1 = Tree([1, 2, 3, 4], [2, 1, 4, 3])
    n1 = t1.make_tree()
    display(n1)
    t1 = Tree()
    n1 = t1.make_tree()
    display(n1)
    t2 = Tree([2, 1, 4, 3], [1, 2, 3, 4])
    n1 = t2.make_tree()
    display(n1)
    t3 = Tree([1, 2, 3], [1, 2, 3])
    n1 = t3.make_tree()
    display(n1)
