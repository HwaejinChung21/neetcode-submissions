class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)
        numbers = []

        for _ in range(len(nums)):
            popped = heapq.heappop(nums)
            numbers.append(-popped)

        return numbers[k - 1]