class Solution:
    '''
    单调栈
    Tricky part:
    
    1. why result = result + (left[i]*right[i]*arr[i])
    e.g. 3,1,2,4 divider can be used to show different subarray:
    3|1|24, 3|12|4, 3|124|, |31|24, |312|4, |3124|
    There are 6 subarrays(# of greater values on the left of 1 * # of greater values on the right of 1) that have "1" as minimum value
    
    2. 用单调栈构建 left right
    
    '''
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left, right = [0]*len(arr), [0]*len(arr)
        stackLeft, stackRight = [], []
        for i in range(len(arr)):
            count = 1
            while stackLeft and stackLeft[-1][0] > arr[i]:
                count += stackLeft.pop()[1]
            left[i] = count
            stackLeft.append((arr[i], count))
        
        for i in range(len(arr)-1, -1, -1):
            count = 1
            while stackRight and stackRight[-1][0] >= arr[i]:
                count += stackRight.pop()[1]
            right[i] = count
            stackRight.append((arr[i], count))
        
        result, mod = 0, 10**9+7
        for i in range(len(arr)):
            result = (result + (arr[i]*left[i]*right[i]))%mod
        return result
    
    