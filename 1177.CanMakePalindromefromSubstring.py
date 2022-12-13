class Solution:
    '''
    prefix sum
    Key points:
    1. we are allowed to rearrange, so we can forget about order and only count the occurences of each letter.
    2. we only care if the count is odd. If it's even, we can place an equal amount of letter on either side:
'aaaac' => 'aacaa'
    3. In order to convert a string to a palindrome using replace, we need only to replace half of the letters. 
    For example:
    'abcd' => 'abba' (4 // 2 = 2)
    'abcde' => 'abcba' (5 // 2 = 2)
    '''
    
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        N = 26
        prefixCounters = [[0]*26]
        for i in range(1, len(s)+1):
            currCounter = prefixCounters[i-1][:]
            c = ord(s[i-1]) - ord('a')
            currCounter[c] += 1
            prefixCounters.append(currCounter)
        
        res = []
        for left, right, k in queries:
            leftCounter, rightCounter = prefixCounters[left], prefixCounters[right+1]
            oddLetters = 0
            for i in range(len(leftCounter)):
                numCurrLetter = rightCounter[i] - leftCounter[i]
                if numCurrLetter % 2 != 0:
                    oddLetters += 1
            if oddLetters // 2 > k:
                res.append(False)
            else:
                res.append(True)
        return res
            
            
        