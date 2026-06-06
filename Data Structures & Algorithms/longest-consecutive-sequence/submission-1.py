class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount = 0
        numSet = set()
        
        for n in nums:
            numSet.add(n)

        for n in nums:
            start = n
            count = 0

            while start in numSet:
                count += 1
                start += 1
            
            maxCount = max(maxCount, count)

        return maxCount