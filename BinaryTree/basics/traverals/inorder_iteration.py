"""
Given a binary tree, traverse the tree in in-order with no recursion.

Time Coplexity: O(N)
Space Complexity: O(N)

"""

def inorderTraversal(root):
    # initialize a stack
    s = []

    curr = root

    while curr != None or len(s) != 0:
        if curr is not None:
            s.append(curr)
            curr = curr.left
        elif len(s) != 0:
            node = s.pop()
            print node.val
            if node.right is not None:
                s.append(node.right)
