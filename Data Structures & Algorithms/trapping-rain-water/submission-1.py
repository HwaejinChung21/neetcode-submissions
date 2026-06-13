class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        maxL = 0
        maxR = 0
        maxArea = 0

        # max left array
        for i in range(len(height)):
            maxLeft[i] = maxL
            maxL = max(maxL, height[i])

        # max right array
        for i in range(len(height) - 1, -1, -1):
            maxRight[i] = maxR
            maxR = max(maxR, height[i])
        
        for i in range(len(height)):
            area = min(maxLeft[i], maxRight[i]) - height[i]

            if area < 0:
                continue

            maxArea += area
            
        return maxArea



            

