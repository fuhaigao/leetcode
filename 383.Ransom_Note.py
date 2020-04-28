class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapping = [0]*26
        for c in magazine:
            index = ord(c)-ord('a')
            mapping[index] += 1
        for c in ransomNote:
            index = ord(c)-ord('a')
            mapping[index] -= 1
            if mapping[index] < 0:
                return False
        return True