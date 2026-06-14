class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = { ")" : "(", "]": "[", "}" : "{" }

        for c in s:
            if c in pMap:
                if not stack:
                    return False
                else:
                    popped = stack.pop()

                    if popped != pMap[c]:
                        return False
            else:
                stack.append(c)

        return not stack

