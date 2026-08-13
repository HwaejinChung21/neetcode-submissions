class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]

        cur.end = True
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.insert(word)

        rows = len(board)
        cols = len(board[0])
        res = []

        def dfs(r, c, node, seen):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            char = board[r][c]

            if char not in node.children:
                return False
            
            if (r, c) in seen:
                return False
            
            seen.add((r, c))
            node = node.children[char]

            if node.end:
                res.append(node.word)
                node.end = False
            
            dfs(r - 1, c, node, seen)
            dfs(r + 1, c, node, seen)
            dfs(r, c - 1, node, seen)
            dfs(r, c + 1, node, seen)
            
            seen.remove((r, c))
            

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root, set())
        
        return res








    
        