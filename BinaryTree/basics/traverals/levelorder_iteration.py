"""
Given a binary tree root node. Traverse the tree in level-order with
no recursion.

Hint: think about using some data structures.

Tree has N nodes.

Solution
    Time Complexity: worst case O(N) average case O(N)
    Space Complexity: worst case O(N) average O(N)

"""


from collections import deque

def levelorderTraversal(root):
    # initialize a double-ended-queue in Python context
    # It is being used because of simplicity. You can always implement
    # your own queue data structure with two stacks or doubly linked list.

    deq = deque()

    # enqueue the root node
    deq.append(root)

    # while queue is not empty

    while len(deq) != 0:
        # dequeue a node at the front and print it
        node = deq.popleft()
        print node.val
        # enqueue left and right child if not None
        if node.left is not None:
            deq.append(node.left)
        if node.right is not None:
            deq.append(node.right)
