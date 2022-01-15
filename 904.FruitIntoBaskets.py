class Solution:
    # Sliding Window
    def totalFruit(self, fruits: List[int]) -> int:
        mapping, count, res, index = dict(), 0, 0, 0
        for i, fruit in enumerate(fruits):
            mapping[fruit] = mapping.get(fruit, 0)+1
            if mapping[fruit] == 1:
                count += 1
            while count > 2:
                mapping[fruits[index]] -= 1
                if mapping[fruits[index]] == 0:
                    count -= 1
                index += 1
            res = max(res, i-index+1)
        return res