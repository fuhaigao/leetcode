class Solution:
    '''
    Greedy
    重点，按 x[1]排序，先insert高的，因为insert矮的不影响高的
    https://programmercarl.com/0406.%E6%A0%B9%E6%8D%AE%E8%BA%AB%E9%AB%98%E9%87%8D%E5%BB%BA%E9%98%9F%E5%88%97.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
    '''
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = list()
        people.sort(key=lambda x:(-x[0],x[1]))
        for person in people:
            index = person[1]
            result.insert(index, person)
        return result