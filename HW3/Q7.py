# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up
# all the values along the path equals the given sum. (Note: A leaf is a node with no children.)
# Example:
# Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# Modify the “solution” class in question7.py, test the above example and design your test case.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)



node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)
node5 = TreeNode(13)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node9 = TreeNode(1)

node1.left = node2
node1.right = node3
node2.left = node4
node4.left = node7
node4.right = node8
node3.left = node5
node3.right = node6
node6.right = node9

print(Solution().hasPathSum(node1, 22))
