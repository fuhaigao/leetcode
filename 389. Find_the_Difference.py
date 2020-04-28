class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ascii_code = 0
        for c in t:
            ascii_code += ord(c)
        for c in s:
            ascii_code -= ord(c)
        return chr(ascii_code)