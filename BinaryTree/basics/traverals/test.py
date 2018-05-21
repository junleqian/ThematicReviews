from inorder_iteration import inorderTraversal as inorderIterative
from inorder_recursion import inorderTraversal as inorderRecursive
from postorder_iteration import postorderTraversal as postorderIterative
from postorder_recursion import postorderTraversal as postorderRecursive
from reverse_postorder_iteration import reversePostorderTraversal as reversePostorderIterative
from levelorder_iteration import levelorderTraversal as levelorderIterative
from test_treenode import TreeNode

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
root.right.right = TreeNode(13)
root.right.left = TreeNode(24)
root.right.left.left = TreeNode(9)
root.right.left.left.left = TreeNode(23)
print "Inorder iteration:"
inorderIterative(root)
print "Inorder recursion:"
inorderRecursive(root)


print "Postorder iteration:"
postorderIterative(root)
print "Postorder recursion:"
postorderRecursive(root)

print "Reverse postorder iteration:"
reversePostorderIterative(root)

print "Levelorder iteration:"
levelorderIterative(root)
