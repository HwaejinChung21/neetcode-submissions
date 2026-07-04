class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxLength = 0
        cSet = set()

        while r < len(s):
            while s[r] in cSet:
                cSet.remove(s[l])
                l += 1

            length = r - l + 1
            maxLength = max(maxLength, length)
            cSet.add(s[r])
            r += 1
        
        return maxLength