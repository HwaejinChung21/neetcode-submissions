class TreeNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TreeNode()
            
            current = current.children[c]
        
        current.endOfWord = True

    def search(self, word: str) -> bool:
        current = self.root

        for c in word:
            if c not in current.children:
                return False
            
            current = current.children[c]

        if current.endOfWord:
            return True
        
        else:
            return False
        
    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for c in prefix:
            if c not in current.children:
                return False
            
            current = current.children[c]

        return True





        
        