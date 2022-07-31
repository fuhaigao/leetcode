class Solution:
    '''
    https://www.youtube.com/watch?v=pS5PaqXa78k
    文字解释不清楚，increasing monolithic stack 是重点
    How to use increasing monolithic stack (单调栈) optimize to O(n)
    1. To solve the problem in O(n), we need to know how many subarray uses current value (arr[i]) as minimum
    2. a. 4,*3,2,1 -> 1 subarray = [3,2,1]
       b. 1,2,*3,4 -> 2 subarrays = [1,2,3], [2,3]
       c. 0,2,*1,4,5,0 -> 6 subarrays = [2,1], [2,1,4], [2,1,4,5], [1], [1,4], [1,4,5]
       therefore, # of subarrays use arr[i] = left * right
    3. we can use increasing monolithic stack to calculate left and right
    
    
    '''
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack, res = [], 0
        for i in range(len(arr)):
            curr = arr[i]
            while stack and curr < arr[stack[-1]]:
                right = stack.pop()
                left = stack[-1] if stack else -1
                res += (right-left)*(i-right)*arr[right]
            stack.append(i)
        
        while stack:
            right = stack.pop()
            left = stack[-1] if stack else -1
            res += (right-left)*(len(arr)-right)*arr[right]
        
        return res % (10**9 + 7)
                
            