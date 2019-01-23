# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        paths = []
        stack = [(root,str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            else:
                if node.left:
                    stack.append((node.left,path + '->' + str(node.left.val)))
                if node.right:
                    stack.append((node.right,path + '->' + str(node.right.val)))
                    
        return paths
