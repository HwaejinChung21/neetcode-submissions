import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        l = 1
        r = k

        while l <= r:
            m = (l + r) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p / m)

            if hours > h:
                l = m + 1
            
            else:
                k = min(k, m)
                r = m - 1

        return k
