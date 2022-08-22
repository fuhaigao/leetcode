class Solution:
    '''
    very similar to 767
    '''
    def rearrangeString(self, s: str, k: int) -> str:
        counter = collections.Counter(s)
        queue = collections.deque([])
        pq = [(-val, key) for key, val in counter.items()]
        heapq.heapify(pq)
        res = []
        idx = 1
        while pq:
            occurence, letter = heapq.heappop(pq)
            res.append(letter)
            queue.append((occurence+1, letter))
            if idx >= k:
                prevOccurence, prevLetter = queue.popleft()
                if prevOccurence < 0:
                    heapq.heappush(pq, (prevOccurence,prevLetter))
            idx += 1
        return "".join(res) if len(res) == len(s) else ""