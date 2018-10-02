"""
Given a binary tree root node, traverse the binary tree in post-order.

class TreeNode(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
"""

def postorderTraversal(root):
    _postorderTraversal(root)
    print ""

def _postorderTraversal(root):
    if root is None:
        return

    if root.left is not None:
        _postorderTraversal(root.left)

    if root.right is not None:
        _postorderTraversal(root.right)

    print "{}".format(root.val),
