class Solution:
    def maxProduct(self, words: List[str]) -> int:
        value = []
        for word in words:
            tmp = 0
            for i in range(len(word)):
                tmp |= 1 << (ord(word[i]) - ord('a'))
            value.append(tmp)
        max_product = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                bit_product = value[i] & value[j]
                if bit_product == 0 and max_product < len(words[i])*len(words[j]):
                    max_product = len(words[i])*len(words[j])
        return max_product