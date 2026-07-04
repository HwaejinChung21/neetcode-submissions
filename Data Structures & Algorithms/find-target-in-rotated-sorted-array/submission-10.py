class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # Are we in the left half of the sorted array?
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                
                else:
                    l = m + 1

            # Are we in the right half of the sorted array?
            # [5,6,1,2,3,4]
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1

                else:
                    r = m - 1
        
        return -1

