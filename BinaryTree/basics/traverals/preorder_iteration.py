"""
Given a binary tree, traverse the tree in preorder with no recursion.
"""

def preorderTraversal(root):
    # initialize a stack
    s = []
    # push the root
    s.append(root)

    # while stack is not empty
    while len(s) != 0:
        # pop a node from the stack
        node = s.pop()
        # print the traversed value
        print node.val
        # push in right child if not None
        if node.left is not None:
            s.append(node.left)
        if node.right is not None:
            s.append(node.right)
