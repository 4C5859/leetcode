/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int max(int a, int b){
    if (a>b) return a;
    else return b;
}
int maxDepth(struct TreeNode* p){
    if (p) return max(1+maxDepth(p->right),1+maxDepth(p->left));
    return 0;
}
int abs1(int a, int b){
    if (a>b) return a-b;
    else return b-a;
}

bool isBalanced(struct TreeNode* root) {
    if (root){
        if (abs1(maxDepth(root->left),(maxDepth(root->right)))<=1) return isBalanced(root->left)&&isBalanced(root->right);
        else return false;
    }
    return true;
    
}
