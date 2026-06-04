class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''
        prefix:
        [1, 1, 2, 8]

        postfix:
        [48, 24, 6, 1]
        '''

        p = 1
        prefix = []
        postfix = []

        for n in nums:
            prefix.append(p)
            p *= n
        
        p = 1

        for i in range(len(nums) - 1, -1, -1):
            prefix[i] *= p
            p *= nums[i]
        
        return prefix