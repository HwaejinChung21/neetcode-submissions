class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:

            # Are we in a fully sorted part of the array?
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            # Are we in the left half of the sorted array?
            if nums[l] <= nums[m]:
                l = m + 1
            
            else:
                r = m - 1

        return res