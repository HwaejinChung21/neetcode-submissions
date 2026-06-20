class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i

            while stack and h < stack[-1][1]:
                i2, h2 = stack.pop()
                area = h2 * (i - i2)
                maxArea = max(maxArea, area)
                start = i2
    
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea