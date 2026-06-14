class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {")" : "(", "]": "[", "}" : "{"}

        for c in s:
            if c in pMap:
                if not stack:
                    return False
                    
                popped = stack.pop()
                print("popped: ", popped)

                if popped != pMap[c]:
                    return False
            else:
                stack.append(c)
            print("stack: ", stack)

        return not stack

