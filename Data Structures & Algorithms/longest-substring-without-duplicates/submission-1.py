class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        r = 0
        maxLength = 0 
        length = 0

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                length -= 1
                
            seen.add(s[r])
            length += 1
            maxLength = max(maxLength, length)
            r += 1

        return maxLength