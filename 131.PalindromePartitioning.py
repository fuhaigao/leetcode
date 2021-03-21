class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.helper(s, 0, [], res)
        return res
        
    def helper(self, s, pos, path, res):
        if len(s) == pos:
            res.append(path)
        for i in range(pos, len(s)):
            if self.is_p(s, pos, i):
                self.helper(s, i+1, path+[s[pos:i+1]], res)

    def is_p(self, s, start, end):
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True