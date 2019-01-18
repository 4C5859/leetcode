/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#define GET_ARRAY_LEN(array,len){len = (sizeof(array) / sizeof(array[0]));}

bool isMirror(struct TreeNode* p,struct TreeNode* q){
    if (!p && !q) return true;
    if (!p || !q) return false;
    return (p->val==q->val)&&(isMirror(p->left,q->right))&&(isMirror(p->right,q->left));
}
bool isSymmetric(struct TreeNode* root) {
    return isMirror(root,root);
}
