class Solution:
    '''
    Tricky Part: result += start
    e.g. a a a b b c c a b c
    when all a, b, c > 0 for first time at j = 5 the n after while loop i will be at i = 3, we will add 3 to result because there would be three substrings from three a's.

    Then a,b,c > 0 at j = 7 ,then we will move i until i = 5 then we will add 5 to result because there could be 5 substrings starting from 0 to second b.
    '''
    def numberOfSubstrings(self, s: str) -> int:
        start, count, result = 0, 0, 0
        counter = collections.defaultdict(int)
        for i in range(len(s)):
            counter[s[i]] += 1
            if counter[s[i]] == 1:
                count += 1
            while count == 3:
                counter[s[start]] -= 1
                if counter[s[start]] == 0:
                    count -= 1
                start += 1
            result += start
        return result