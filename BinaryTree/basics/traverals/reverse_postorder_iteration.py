"""
Given a binary tree root, traverse the tree in reverse-post-order without
using recursion.

Hint: think about the second stack used in iterative postorder traversal.
Do you still need a second stack?

"""

def reversePostorderTraversal(root):
    # initialize s1 and append the root node
    s1 = []
    s1.append(root)

    while len(s1) != 0:
      # while s1 is not empty, pop a node from s1
      node = s1.pop()
      # instead of storing it into a second stack, just print it
      print node.val
      # push left, right into the s1
      s1.append(node.left) if node.left is not None
      s1.append(node.right) if node.left is not None
