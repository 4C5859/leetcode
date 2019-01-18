# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def ist(p,q):
            if p and q:
                if p.val == q.val:
                    if ist(p.left,q.left):
                        if ist(p.right,q.right):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            
            if not p and q:
                return False
            if p and not q:
                return False
            return True
        return ist(p,q)
