"""
Given a binary tree root node. Traverse the tree in post-order without
recursion.

Hint: use more stacks

O(N)
O(N)

"""

def postorderTraversal(root):
    # initialize two stacks
    s1 = []
    s2 = []

    # push root into s1
    s1.append(root)

    # while s1 is not empty
    while len(s1) != 0:
        # pop the top of the s1
        node = s1.pop()
        # push node into s2
        s2.append(node)
        # push left child of the node if not empty to s1
        if node.left is not None:
            s1.append(node)
        if node.right is not None:
            s1.append(node)

    # nodes stored in s2 are already in reverse-post-order
    # pop each of them and print to print the post-order traversal
    while len(s2) != 0:
        node = s2.pop()
        print node.val
