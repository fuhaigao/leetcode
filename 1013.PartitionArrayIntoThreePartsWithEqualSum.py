class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        arrSum = sum(arr)
        if arrSum % 3 != 0:
            return False
        target = arrSum // 3
        currSum = 0
        count = 0
        for num in arr:
            currSum += num
            if currSum == target:
                currSum = 0
                count += 1
        return count >= 3