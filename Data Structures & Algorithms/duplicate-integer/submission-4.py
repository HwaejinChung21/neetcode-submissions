class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()

        for n in nums:
            if n in duplicates:
                return True
            
            duplicates.add(n)

        return False
        