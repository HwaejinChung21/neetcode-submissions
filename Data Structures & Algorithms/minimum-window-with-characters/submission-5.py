class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        sMap = {}
        tMap = {}
        l, r = 0, 0
        res = [0, 0]
        bestLength = float("inf")

        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)

        need = len(tMap)
        have = 0

        while r < len(s):
            # skip over ones we don't need
            if s[r] in tMap:
                sMap[s[r]] = 1 + sMap.get(s[r], 0)

                if sMap[s[r]] == tMap.get(s[r], 0):
                    have += 1

            while have == need:
                curLength = r - l + 1

                if curLength < bestLength:
                    bestLength = min(bestLength, curLength)
                    res = [l, r]

                if s[l] in tMap:
                    sMap[s[l]] -= 1

                    if sMap[s[l]] < tMap[s[l]]:
                        have -= 1
            
                l += 1
            
            r += 1

        left = res[0]
        right = res[1]

        return "" if bestLength == float("inf") else s[left:right + 1]
