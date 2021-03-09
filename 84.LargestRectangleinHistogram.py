class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        heights.append(0)
        stack = [-1]
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] -1
                res = max(res, height*width)
            stack.append(i)
        heights.pop()
        return res

