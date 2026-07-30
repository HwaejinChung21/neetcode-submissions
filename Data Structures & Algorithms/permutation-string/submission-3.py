class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map = {}
        s2Map = {}

        for i in range(len(s1)):
            s1Map[s1[i]] = 1 + s1Map.get(s1[i], 0)
            s2Map[s2[i]] = 1 + s2Map.get(s2[i], 0)

        if s1Map == s2Map:
            return True
        
        for i in range(len(s1), len(s2)):
            s2Map[s2[i]] = 1 + s2Map.get(s2[i], 0)
            s2Map[s2[i - len(s1)]] -= 1
            
            if s2Map[s2[i - len(s1)]] == 0:
                del s2Map[s2[i - len(s1)]]

            if s1Map == s2Map:
                return True
        
        return False

        