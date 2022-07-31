class Solution:
    # Two pointer!
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for query in queries:
            res.append(self.compare(query, pattern))
        return res
    
    def compare(self, query, pattern):
        i = 0
        for c in query:
            if i<len(pattern) and c == pattern[i]:
                i += 1
            elif c.isupper():
                return False
        return i == len(pattern)