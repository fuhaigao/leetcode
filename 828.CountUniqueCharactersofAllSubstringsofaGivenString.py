class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # 累似907, use dictionary instead of monolithic stack
        # https://www.youtube.com/watch?v=Ynt0-zzQcZc
        letters, res = dict(), 0
        for i in range(len(s)):
            curr = s[i]
            if curr in letters:
                left = letters[curr][0]
                right = letters[curr][1]
                res += (right-left) * (i-right)
                letters[curr] = [right, i]
            else:
                letters[curr] = [-1, i]
        print(letters)
        for ranges in letters.values():
            left, right = ranges[0], ranges[1]
            res += (right-left) * (len(s)-right)
        return res
            