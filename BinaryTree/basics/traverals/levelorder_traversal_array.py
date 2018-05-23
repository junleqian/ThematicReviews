"""
Given a binary tree, write a program to return
its levels in array ( or ArrayList).
For example,
   1
3    4
will have you return [ [1], [3, 4] ]
"""



def level_order_array(root):
    if root is None:
        return []

    levels = []
    current_level = [root]


    while len(current_level) != 0:
        next_level = []
        current_level_vals = []
        for node in current_level:
            current_level_vals.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        # append the new level with values
        levels.append(current_level_vals)
        current_level = next_level

    return levels


def level_order_array_bottom(root):
    return level_order_array(root)[::-1]
