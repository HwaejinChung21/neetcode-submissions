class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = float("inf")

        while l <= r:
            # Array fully sorted already
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break

            m = (l + r) // 2
            minimum = min(minimum, nums[m])

            # We are in left half of the sorted array
            if nums[m] >= nums[l]:
                l = m + 1

            # We are in right half of sorted array
            else:
                r = m - 1

        return minimum


