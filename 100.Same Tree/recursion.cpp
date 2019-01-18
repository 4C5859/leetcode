/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    if (p && q){
        if (p->val != q->val) return false;
        else {
            if (isSameTree(p->left,q->left)){
                if (isSameTree(p->right,q->right)) return true;
                else return false;
            }
            else return false;
        }
    }
    if (p && !q) return false;
    if (!p && q) return false;
    return true;
    
}
