class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        if name[0] != typed[0]:
            return False
        while i<len(name) and j < len(typed):
            if name[i] != typed[j]:
                if typed[j] != typed[j-1]:
                    return False
                j += 1
            else:
                i, j = i+1, j+1
        for x in range(j, len(typed)):
            if typed[x] != typed[x-1]:
                return False
        return i == len(name)

# Cleaner code
    # def isLongPressedName(self, name, typed):
    #     i = 0
    #     for j in range(len(typed)):
    #         if i < len(name) and name[i] == typed[j]:
    #             i += 1
    #         elif j == 0 or typed[j] != typed[j - 1]:
    #             return False
    #     return i == len(name)