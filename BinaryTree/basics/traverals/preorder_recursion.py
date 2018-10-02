"""
Given a binary tree root node, traverse the binary tree in pre-order.

class TreeNode(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
"""
def preorderTraversal(root):
    _preorderTraversal(root)
    print ""


def _preorderTraversal(root):
    if root is None:
        return

    print "{}".format(root.val),

    if root.left is not None:
        _preorderTraversal(root.left)

    if root.right is not None:
        _preorderTraversal(root.right)
