# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_path_sum = -2**32
    
    def helperTraversal(self, node):
        if not node:
            return 0
        
        left = self.helperTraversal(node.left)
        right = self.helperTraversal(node.right)
        
        self.max_path_sum = max(self.max_path_sum, node.val + left + right)
        
        max_path = max(left, right) + node.val
        return max_path if max_path > 0 else 0
        
    def maxPathSum(self, root: TreeNode) -> int:
        self.helperTraversal(root)
        return self.max_path_sum