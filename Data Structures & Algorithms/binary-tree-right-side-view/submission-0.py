# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = collections.deque()
        q.append(root)

        while q:
            level = []

            for i in range(len(q)):
                popped = q.popleft()
                level.append(popped.val)

                if popped.left:
                    q.append(popped.left)
                
                if popped.right:
                    q.append(popped.right)

            res.append(level[-1])

        return res
                    

