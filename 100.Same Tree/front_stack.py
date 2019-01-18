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
        if not p and not q:
            return True
        if not p and q:
            return False
        if  p and not q:
            return False
        stackp = []
        stackq = []
        nodep = p;
        nodeq = q;
        while (nodep or stackp) and (nodeq or stackq):
            while nodep and nodeq:
                if nodep.val == nodeq.val:
                    stackp.append(nodep)
                    stackq.append(nodeq)
                    nodep = nodep.left
                    nodeq = nodeq.left
                else:
                    return False
            if nodep == None and nodeq == None:
                nodep = stackp.pop()
                nodeq = stackq.pop()
                nodep = nodep.right
                nodeq = nodeq.right
            else:
                return False
        return True
