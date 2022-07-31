class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        topCount, bottomCount = [0]*7, [0]*7
        same = [0]*7
        for i in range(len(tops)):
            topCount[tops[i]] += 1
            bottomCount[bottoms[i]] += 1
            if tops[i] == bottoms[i]:
                same[tops[i]] += 1
        for i in range(1, 7):
            if topCount[i] + bottomCount[i] - same[i] == len(tops):
                return min(topCount[i], bottomCount[i]) - same[i]
        return -1