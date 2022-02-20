class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        results = [0]*(length+1)
        for start, end, inc in updates:
            results[start] += inc
            results[end+1] -= inc
        
        for i in range(1, length+1):
            results[i] += results[i-1]
        return results[:length]