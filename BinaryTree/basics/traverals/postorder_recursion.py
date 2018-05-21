"""
Given a binary tree root node, traverse the binary tree in post-order.

class TreeNode(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
"""

def postorderTraversal(root):
    if root is None:
        return

    if root.left is not None:
        postorderTraversal(root.left)

    if root.right is not None:
        postorderTraversal(root.right)

    print root.val
