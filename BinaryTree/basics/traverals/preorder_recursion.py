"""
Given a binary tree root node, traverse the binary tree in pre-order.

class TreeNode(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
"""

def preorderTraveral(root):
    if root is None:
        return

    print root.val

    if root.left is not None:
        preorderTraversal(root.left)

    if root.right is not None:
        preorderTraversal(root.right)
