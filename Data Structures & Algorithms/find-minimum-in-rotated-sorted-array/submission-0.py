class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = float("inf")

        while l < r:
            m = (l + r) // 2

            # Array fully sorted already
            if nums[l] < nums[r]:
                return nums[l]

            # We are in right half of sorted array
            elif nums[m] < nums[r]:
                r = m 

            # We are in left half of the sorted array
            elif nums[m] > nums[r]:
                l = m + 1

        return nums[l]


