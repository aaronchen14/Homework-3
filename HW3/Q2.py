# Given a binary tree, find the max depth of it. Modify the “solution” function in the question2.py
# (Analyze your time complexity, and only time-complexity optimized solution gets full grade)


class TreeNode(object):
    # """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def solution(root):
    # '''type in your solution'''
    if root.left is None and root.right is None:
        return True

    depth = max(solution(root.left), solution(root.right)) + 1
    return depth


a15 = TreeNode(15)
a7 = TreeNode(7)
a20 = TreeNode(20)
a9 = TreeNode(9)
a3 = TreeNode(3)
a20.left = a15
a20.right = a7
a3.left = a9
a3.right = a20
print(solution(a3))

# Since the node is only examined once, the time complexity is O(n).
