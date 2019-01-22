# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isAncestor(self, a, b):
        if not a:
            return False
        if a==b:
            return True
        return self.isAncestor(a.left,b) or self.isAncestor(a.right,b)
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        h1 = self.isAncestor(p,q)
        if h1:
            return p
        h2 = self.isAncestor(q,p)
        if h2:
            return q
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left and node.right:
                if self.isAncestor(node.left,p) and self.isAncestor(node.right,q):
                    return node
                if self.isAncestor(node.left,q) and self.isAncestor(node.right,p):
                    return node
                if self.isAncestor(node.left,p) and self.isAncestor(node.left,q):
                    queue.append(node.left)
                if self.isAncestor(node.right,p) and self.isAncestor(node.right,q):
                    queue.append(node.right)
            if not node.right and node.left:
                queue.append(node.left)
            if not node.left and node.right:
                queue.append(node.right)
