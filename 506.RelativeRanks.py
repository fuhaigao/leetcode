class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pairs = []
        for i in range(len(score)):
            pairs.append((score[i], i))
        pairs.sort(key = lambda x: -x[0])
        result = [0]*len(pairs)
        for i in range(len(pairs)):
            val, index = pairs[i]
            if i == 0:
                result[index] = "Gold Medal"
            elif i == 1:
                result[index] = "Silver Medal"
            elif i == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(i+1)
        return result
            