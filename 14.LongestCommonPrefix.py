class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs:
            prefix = self.check_prefix(prefix, s)
        return prefix
    
    def check_prefix(self, prefix, string):
        length = 0
        while length < len(prefix) and length < len(string):
            if prefix[length] == string[length]:
                length += 1
            else:
                break
        return prefix[0:length]