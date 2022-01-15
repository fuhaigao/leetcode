class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapping = dict()
        for i in range(len(s)):
            mapping[s[i]] = i
        start, end = 0, 0 
        result = []
        for i in range(len(s)):
            end = max(end, mapping[s[i]])
            if i == end:
                result.append(end-start+1)
                start = end+1
        return result