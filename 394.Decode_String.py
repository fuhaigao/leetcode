class Solution:
    def decodeString(self, s: str) -> str:
        curr_str = ""
        str_stack = []
        num_stack = []
        res = ""
        count = 0
        
        for c in s:
            if c.isdigit():
                count = count*10 + int(c)
            elif c == '[':
                num_stack.append(count)
                count = 0
                str_stack.append(curr_str)
                curr_str = ""
            elif c == ']':
                num = num_stack.pop()
                prev_str = str_stack.pop()
                curr_str = prev_str +  num* curr_str
            else:
                curr_str += c
        return curr_str
    
        