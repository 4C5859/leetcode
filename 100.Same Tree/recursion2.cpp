/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    if (!p && !q) return true;
    if (!p || !q || p->val!=q->val) return false;
    bool left = isSameTree(p->left,q->left);
    bool right = isSameTree(p->right,q->right);
    return left && right;
}
