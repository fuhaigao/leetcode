class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for c in s:
            dict1[c] = dict1.get(c, 0) + 1
        for c in t:
            dict2[c] = dict2.get(c, 0) + 1
        return dict1 == dict2
        
    # def isAnagram(self, s: str, t: str) -> bool:
    #     alphabet = [0]*26
    #     for i in range(max(len(s), len(t))):
    #         if i < len(s):
    #             alphabet[ord(s[i]) - ord('a')] += 1
    #         if i < len(t):
    #             alphabet[ord(t[i]) - ord('a')] -= 1
    #     for val in alphabet:
    #         if val != 0:
    #             return False
    #     return True