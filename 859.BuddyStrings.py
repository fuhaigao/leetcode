class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal and len(set(s)) != len(s):
            return True
        s, goal = list(s), list(goal)
        start = -1
        for i in range(len(s)):
            if s[i] != goal[i]:
                if start != -1:
                    s[start], s[i] = s[i], s[start]
                    return str(s) == str(goal)
                else:
                    start = i
        return False
