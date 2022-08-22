class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            # sorted return a list of sorted chars, need to convert it to a tuple / string to use it as a dictionary key
            d[tuple(sorted(s))].append(s)
        return list(d.values())