class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            if l < r and numbers[l] + numbers[r] > target:
                r -= 1
            if l < r and numbers[l] + numbers[r] < target:
                l += 1
            if l < r and numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
                

  
        