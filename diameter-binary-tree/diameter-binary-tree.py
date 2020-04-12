# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(root, ans):
            if not root:
                return 0
            
            left_h = height(root.left, ans)
            right_h = height(root.right, ans)
            
            ans[0] = max(ans[0], left_h + right_h)
            
            return 1 + max(left_h, right_h)
            
        if not root:
            return 0
        
        ans = [-999999999999]
        
        height_of_root = height(root, ans)
        
        return ans[0]