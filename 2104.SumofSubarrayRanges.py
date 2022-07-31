class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        increaseStack, decreaseStack, res = [], [], 0
        for i in range(len(nums)):
            curr = nums[i]
            while increaseStack and curr < nums[increaseStack[-1]]:
                right = increaseStack.pop()
                left = increaseStack[-1] if increaseStack else -1
                res -= (right-left)*(i-right)*nums[right]
            while decreaseStack and curr > nums[decreaseStack[-1]]:
                right = decreaseStack.pop()
                left = decreaseStack[-1] if decreaseStack else -1
                res += (right-left)*(i-right)*nums[right]
            
            increaseStack.append(i)
            decreaseStack.append(i)
            
        while increaseStack:
            right = increaseStack.pop()
            left = increaseStack[-1] if increaseStack else -1
            res -= (right-left)*(len(nums)-right)*nums[right]
            
        while decreaseStack:
            right = decreaseStack.pop()
            left = decreaseStack[-1] if decreaseStack else -1
            res += (right-left)*(len(nums)-right)*nums[right]
        return res