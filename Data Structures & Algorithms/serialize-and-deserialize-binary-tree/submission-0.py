# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = ""

        def dfs(node):
            if not node:
                self.res += "N,"
                return
            
            self.res += str(node.val) + ","
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.i = 0

        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None
            
            newNode = TreeNode(int(values[self.i]))
            self.i += 1
            newNode.left = dfs()
            newNode.right = dfs()
            return newNode
        
        return dfs()



