class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.endWord = ""
    

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
        cur.endWord = word
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.insert(word)

        rows = len(board)
        cols = len(board[0])
        res = []

        def dfs(row, col, node, seen):

            char = board[row][col]

            if char not in node.children or (row, col) in seen:
                return False
            
            node = node.children[char]
            if node.end:
                node.end = False
                res.append(node.endWord)
            
            seen.add((row, col))

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for i, j in directions:
                if row + i < 0 or row + i >= rows or col + j < 0 or col + j >= cols:
                    continue

                dfs(row + i, col + j, node, seen)

            seen.remove((row, col))
        

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root, set())

        return res





        




        