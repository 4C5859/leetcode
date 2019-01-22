# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self,root):
        if root:
            return max(self.maxDepth(root.left)+1,self.maxDepth(root.right)+1)
        return 0;
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if abs(self.maxDepth(root.left)-self.maxDepth(root.right))<=1:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
            else:
                return False
        return True
