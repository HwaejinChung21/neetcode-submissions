class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        while k > 0:
            popped = heapq.heappop(nums) 
            k -= 1 

            if k == 0:
                return -popped