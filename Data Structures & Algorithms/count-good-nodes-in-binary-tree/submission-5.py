# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, biggest):
            if not node:
                return 0
            
            if node.val >= root.val and node.val >= biggest.val:
                print(biggest.val)
                biggest = node
                self.count += 1
            
            dfs(node.left, biggest)
            dfs(node.right, biggest)
        
        dfs(root, root)
        return self.count