# Accepted, but disappointingly only faster than 5% of Python submissions.
import numpy as np
import operator as op
from functools import reduce
from typing import List
from algorith.leetc.trees.tree_node import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, key):
        self.key = int(key)
        self.val = int(key)
        self.right = None
        self.left = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return print_all_trees(n)


def ncr(n, r):
    if r < 0:
        return 0
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


def n_catalan2(h, t):
    if t < 0:
        return 0
    elif t == 0:
        return 1
    else:
        return abs(ncr(h+t-1, t) - ncr(h+t-1, t-1))


def ix_to_path(ix, h, t):
    """
    Given an index, returns the Dyck path.
    args:
        ix: The index to be converted.
        t: The number of tails in the path.
        h: The number of heads in the path.
    """
    v = ix
    path = np.zeros(t + h)
    for i in range(t+h):
        tail_paths = n_catalan2(h, t-1)
        if v >= tail_paths:
            path[i] = 1
            h -= 1
            v -= tail_paths
            if h == 0:
                break
        else:
            t -= 1
    return path


def get_tree(path, start, end):
    if end <= start:
        return None
    targ = path[start]
    x = find_tar(path, targ, start)
    root = TreeNode((x-start)/2)
    root.left = get_tree(path, start+1, x-1)
    root.right = get_tree(path, x, end)
    # Fix the labels of the keys.
    return root


def get_tree2(path):
    root = get_tree(path, 0, len(path)-1)
    Tr(root)
    return root


class Tr():
    def __init__(self, x):
        self.i = 1
        self.root = self.label_inorder(x)

    def label_inorder(self, x):
        if x is not None:
            self.label_inorder(x.left)
            x.key = self.i
            x.val = self.i
            self.i += 1
            self.label_inorder(x.right)


class Tr1():
    def __init__(self, root):
        self.root = root
        self.arr = []
        self.tree_to_array(root)

    def tree_to_array(self, tn):
        """
        Converts tree to leetcode array.
        """
        if tn is not None:
            self.arr.append(tn.key)
        else:
            self.arr.append(None)
        if tn is not None and\
           (tn.left is not None or tn.right is not None):
            self.tree_to_array(tn.left)
            self.tree_to_array(tn.right)


def print_all_trees(n=3):
    n_trees = n_catalan2(n, n+1)
    trees = []
    for ix in range(n_trees):
        tn = ix_to_tree(ix, n)
        trees.append(tn)
    return trees


def ix_to_tree(ix, n):
    """
    Converts index to lexicographic binary search tree.
    args:
        ix: The index.
        n: The number of nodes in the tree.
    """
    path = ix_to_path(ix, n, n+1)
    # The last entry is a redundant tail. So, remove it.
    tree_nd = print_tree(path[:len(path)-1])
    return tree_nd


def print_tree(path=[1, 1, 1, 0, 0, 0]):
    for i in range(len(path)):
        if path[i] == 0:
            path[i] = -1
    path = np.concatenate(([0], np.cumsum(path)))
    tn = get_tree2(path)
    return tn


def find_tar(path, targ, start):
    i = start+1
    while path[i] != targ:
        i += 1
    return i


if __name__=="__main__":
    sol = Solution()
    sol.generateTrees(3)
