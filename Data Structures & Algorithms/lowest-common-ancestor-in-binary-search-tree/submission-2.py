# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.lowest = root

        if p.val < root.val and q.val < root.val:
            # search left
            self.lowestCommonAncestor(root.left, p, q)
        
        elif p.val > root.val and q.val > root.val:
            # search right
            self.lowestCommonAncestor(root.right, p, q)
        
        else:
            self.lowest = root
        
        return self.lowest

    
    # a node is an ancestor if both p and q are its descendants,
    # when we find an ancestor, we record, then decide whether to go left or right

        
            