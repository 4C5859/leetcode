# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution:
    def ConstructTree(self,nums,start,end):
            if start == end:
                return TreeNode(nums[start])
            if start > end:
                return None
            mid = (start+end)//2
            root = TreeNode(nums[mid])
            root.left = self.ConstructTree(nums,start,mid-1)
            root.right = self.ConstructTree(nums,mid+1,end)     
            return root
        
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.ConstructTree(nums,0,len(nums)-1)
                
