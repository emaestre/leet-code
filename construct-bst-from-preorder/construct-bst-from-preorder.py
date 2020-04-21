# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        def bstInsert(node: TreeNode, val: int) -> TreeNode:
            temp = node
            if node is None:
                newNode = TreeNode(val)
                node = newNode
                return node
            
            if val < node.val:
                node.left = bstInsert(temp.left, val)
            
            if val > node.val:
                node.right = bstInsert(temp.right, val)
                
            return node
        
        node = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            bstInsert(node, preorder[i])
        
        return node