class Solution:
    '''
    Simple DP + Greedy
    
    memorize the most valuable item during ieration
    most valuable item = values[i] + i
    each time, max score = values[i] + most valuable item + index of most valuable item - i
    '''
    # 
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxScore = -1
        currMaxIndex= 0
        for i in range(1, len(values)):
            maxScore = max(maxScore, values[i]+values[currMaxIndex]+currMaxIndex-i)
            if values[i]+i > values[currMaxIndex]+currMaxIndex:
                currMaxIndex = i
        return maxScore