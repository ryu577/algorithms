from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        self.preorder = preorder
        self.inorder = inorder
        self.n = len(preorder)
        self.ixx = -1
        return self.make_tree(0, self.n - 1)

    def findin(self, rix, start, end):
        for i in range(start, end + 1):
            if self.inorder[i] == rix:
                return i
        return -1

    def make_tree(self, start, end):
        if end < start:
            return None
        # Only update ixx when a valid node is returned.
        self.ixx += 1
        if end == start:
            return TreeNode(self.inorder[start])
        root_ix = self.preorder[self.ixx]
        fix = self.findin(root_ix, start, end)
        root = TreeNode(root_ix)
        root.left = self.make_tree(start, fix - 1)
        root.right = self.make_tree(fix + 1, end)
        return root
