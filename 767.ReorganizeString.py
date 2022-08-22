class Solution:
    '''
    https://leetcode.com/problems/reorganize-string/discuss/113457/Simple-python-solution-using-PriorityQueue
    '''
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        pq = [(-val, key) for key, val in counter.items()]
        heapq.heapify(pq)
        res, prevOccurence, prevLetter = [], 0, ""
        while pq:
            occurence, letter = heapq.heappop(pq)
            res.append(letter)
            occurence +=1
            if prevOccurence < 0:
                heapq.heappush(pq, (prevOccurence, prevLetter))
            prevOccurence, prevLetter = occurence, letter
        return "".join(res) if len(res) == len(s) else ""