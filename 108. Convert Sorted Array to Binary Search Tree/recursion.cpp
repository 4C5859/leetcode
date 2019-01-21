/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode *ConstructTree(int *nums, int start, int end){
    struct TreeNode *root;
    root = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    int mid;
    if (start>end) return NULL;
    if (start==end){
        root->val = nums[start];
        root->left = NULL;
        root->right = NULL;
        return root;
    }
    mid = (end-start)/2 + start;
    root->val = nums[mid];
    root->left = ConstructTree(nums,start, mid-1);
    root->right = ConstructTree(nums,mid+1,end);
    return root;
}
struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    return ConstructTree(nums, 0, numsSize-1);
}
