class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x:x[1])
        currTail = float("-inf")
        length = 0
        for pair in pairs:
            if pair[0] > currTail:
                currTail = pair[1]
                length += 1
        return length