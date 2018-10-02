"""
Given a binary tree root node, traverse the binary tree in in-order.

class TreeNode(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

solution Complexity
Time: O(N)
Space: O(N) on function stack

"""

def inorderTraversal(root):
    _inorderTraversal(root)
    print ""


def _inorderTraversal(root):
    if root is None:
        return

    if root.left is not None:
        _inorderTraversal(root.left)

    print "{}".format(root.val),

    if root.right is not None:
        _inorderTraversal(root.right)
