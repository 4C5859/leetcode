/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* invertTree(struct TreeNode* root) {
    if (!root) return NULL;
    struct TreeNode* node;
    node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = root->val;
    node->left = invertTree(root->right);
    node->right = invertTree(root->left);
    return node;
}
