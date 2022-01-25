class Solution:
    '''
    单调栈
    tricky part: stack initialize with -1, and append heights with 0. 
    This way, stack won't be empty for getting width, and heights[-1] will be also considered
    '''
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

