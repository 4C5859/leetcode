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
        def constructPaths(root,path):
            if root:
                path = path + str(root.val)
                if not root.right and not root.left:
                    paths.append(path)
                else:
                    path = path + '->'
                    constructPaths(root.left,path)
                    constructPaths(root.right,path)
        paths = []
        constructPaths(root,'')
        return paths
