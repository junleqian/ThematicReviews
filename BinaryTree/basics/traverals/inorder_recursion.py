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
    if root is None:
        return

    if root.left is not None:
        inorderTraversal(root.left)

    print root.val

    if root.right is not None:
        inorderTraversal(root.right)
