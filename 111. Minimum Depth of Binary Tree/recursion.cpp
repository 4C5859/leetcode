/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int min(int a, int b){
    if (a<b) return a;
    else return b;
}
int minDepth(struct TreeNode* root) {
    if (!root) return 0;
    if (!root->left && !root->right) return 1;
    if (!root->left) return minDepth(root->right)+1;
    if (!root->right) return minDepth(root->left)+1;
    return min(1+minDepth(root->left),1+minDepth(root->right));
    
}
