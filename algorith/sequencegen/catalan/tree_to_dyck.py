import numpy as np
from algorith.sequencegen.catalan.next_tree import ix_to_tree
from algorith.sequencegen.catalan.next_dyck import n_catalan2


class TreeToDyck():
    def __init__(self, node, n):
        self.path = np.ones(2*n)
        self.path[2*n-1] = -1
        self.tree_to_dyck(node, 1, 2*n)

    def tree_to_dyck(self, node, st, ed):
        if node is None or st >= ed:
            return
        self.path[st+2*node.key-2] = -1
        self.tree_to_dyck(node.left, st+1, ed-1)
        self.tree_to_dyck(node.right, st, ed)


def tst():
    nn = n_catalan2(6, 7)
    ix = np.random.choice(nn)
    print(ix)
    node, path = ix_to_tree(ix, 6)
    node.display()
    print(path)
    td = TreeToDyck(node, 6)
    print(td.path)


if __name__ == "__main__":
    tst()
