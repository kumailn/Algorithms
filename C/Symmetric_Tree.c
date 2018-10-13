bool isSymmetric(struct TreeNode* root) {
    if(!root) return true;
    bool help(struct TreeNode* l, struct TreeNode* r){
        if(!l && !r) return true;
        if(l && r && l->val != r->val) return false;
        if(!l || !r) return false;
        return help(l->left, r->right) && help(l->right, r->left);
    };
    return help(root->left, root->right);
}