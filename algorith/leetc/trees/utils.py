import numpy as np
from algorith.leetc.trees.unique_bst_2 import TreeNode1
from algorith.leetc.trees.pprint import display


def arr_2_tree(a=[1,2,2,3,4,4,3]):
	nodes = []

	for i in a:
		nodes.append(TreeNode1(i))

	for i in range(len(a)):
		n = nodes[int((i-1)/2)]
		if i%2 == 0:
			n.left = nodes[i]
		else:
			n.right = nodes[i]

	display(nodes[0])
	return nodes[0]


