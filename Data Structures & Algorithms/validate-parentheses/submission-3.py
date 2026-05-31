class Solution:
    def isValid(self, s: str) -> bool:
        pMap = { "}" : "{", "]" : "[", ")" : "(" }
        stack = []

        for char in s:
            if char not in pMap:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:      
                    popped = stack.pop()
                    if popped != pMap[char]:
                        return False
        
        return not stack