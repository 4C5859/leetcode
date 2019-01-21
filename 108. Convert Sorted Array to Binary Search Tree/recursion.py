# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.result = []
        if not nums:
            return self.result
        root = []
        def ConstructTree(root,nums):
            if not nums:
                return None
            if len(nums) == 1:
                root = TreeNode(nums[0])
                return root
            if len(nums) == 2:
                root = TreeNode(nums[1])
                root.left = TreeNode(nums[0])
                return root
            if len(nums) == 3:
                root = TreeNode(nums[1])
                root.left = TreeNode(nums[0])
                root.right = TreeNode(nums[2])
                return root
            root = TreeNode(nums[len(nums)//2])
            root.left = ConstructTree(root,nums[0:len(nums)//2])
            root.right = ConstructTree(root,nums[len(nums)//2+1:len(nums)])
            return root
        return ConstructTree(root,nums)
