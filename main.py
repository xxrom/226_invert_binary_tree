from typing import List


class Node:

  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def printTree(self, root: Node, points: List[int] = []) -> List[int]:
    if root is not None:
      points.append(root.val)
      if root.left is not None:
        self.printTree(root.left, points)
      if root.right is not None:
        self.printTree(root.right, points)
    else:
      points.append(None)

    return points

  def invertTree(self, root: Node) -> Node:
    if root is not None:
      temp = root.left
      root.left = root.right
      root.right = temp

      if root.right is not None:
        self.invertTree(root.right)
      if root.left is not None:
        self.invertTree(root.left)

    return root


my = Solution()
t0 = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(6), Node(9)))
print(my.printTree(t0, []))
ans = my.invertTree(t0)
print('ans %s' % str(ans))
print(my.printTree(ans, []))

#           1
#         2   4
#        3   5
