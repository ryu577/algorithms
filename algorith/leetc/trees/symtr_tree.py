import numpy as np
import collections
from algorith.leetc.trees.utils import arr_2_tree
# https://leetcode.com/problems/symmetric-tree/
# Solutions taken from: 
# https://leetcode.com/problems/symmetric-tree/solutions/33050/Recursively-and-iteratively-solution-in-Python/

class Solution1:
    def isSymmetric(self, root):
        if not root:
            return True
        
        q = collections.deque([root.left, root.right])
        
        while q:
            t1, t2 = q.popleft(), q.popleft()

            if not t1 and not t2:
                continue
            elif (not t1 or not t2) or (t1.val != t2.val):
                return False
            
            q += [t1.left, t2.right, t1.right, t2.left]
            
        return True


class Solution2:
  def isSymmetric(self, root):
    if root is None:
      return True
    else:
      return self.isMirror(root.left, root.right)

  def isMirror(self, left, right):
    if left is None and right is None:
      return True
    if left is None or right is None:
      return False

    if left.val == right.val:
      outPair = self.isMirror(left.left, right.right)
      inPiar = self.isMirror(left.right, right.left)
      return outPair and inPiar
    else:
      return False


def tst():
	n1 = arr_2_tree([1,2,2,3,4,4,3])
	s1 = Solution1().isSymmetric(n1)
	print(s1)

