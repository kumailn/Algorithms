var isSymmetric = function(root) {
    if(!root) return true;
    let help = (l, r) => {
        if (!l && !r) return true;
        if (l && r && l.val != r.val) return false;
        if (!l || !r) return false;
        return help(l.right, r.left) && help(l.left, r.right);
    }
    return help(root.left, root.right);
};