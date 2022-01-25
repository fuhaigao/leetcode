class Solution:
    '''
    在原list上进行修改，用two pointers
    '''
    def compress(self, chars: List[str]) -> int:
        slow, fast = 0, 0
        while fast <= len(chars)-1:
            chars[slow] = chars[fast]
            slow += 1
            count = 1
            while fast <= len(chars)-2 and chars[fast] == chars[fast+1]:
                fast += 1
                count += 1
            if count > 1:
                for c in str(count):
                    chars[slow] = c
                    slow += 1
            fast += 1
        return slow