class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0]*(length+1)
        for update in updates:
            res[update[0]] += update[2]
            res[update[1]+1] -= update[2]
        for i in range(length):
            res[i+1] += res[i]
        return res[:length]
