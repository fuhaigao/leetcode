class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = [0 for i in range(len(height))], [0]*len(height)
        currMax = 0
        for i in range(len(height)):
            if height[i] <= currMax:
                left[i] = currMax
            else:
                currMax = height[i]
                left[i] = currMax
        currMax = 0

        for i in range(len(height)-1, -1, -1):
            if height[i] > currMax:
                currMax = height[i]
            right[i] = currMax
        
        sum = 0
        for i in range(len(height)):
            sum += min(left[i], right[i]) - height[i]
        
        return sum