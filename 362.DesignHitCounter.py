'''
Assumption: 
1. timestamp in hit is always greater than previous hit call
2. timestamp in getHits will be recent 5 mins

Initial idea: manage a queue to keep pushing the coming hit
problem: if huge amount of hits happened at the same timestamp, this solution will takes too much memory since each element in queue is a single hit.

Solution
https://leetcode.com/problems/design-hit-counter/discuss/83483/Super-easy-design-O(1)-hit()-O(s)-getHits()-no-fancy-data-structure-is-needed!
'''


class HitCounter:

    def __init__(self):
        self.timestamps = [0]*300
        self.counter = [0]*300

    def hit(self, timestamp: int) -> None:
        index = timestamp % 300
        if self.timestamps[index] != timestamp:
            self.timestamps[index] = timestamp
            self.counter[index] = 1
        else:
            self.counter[index] += 1

    def getHits(self, timestamp: int) -> int:
        res = 0
        for i in range(len(self.counter)):
            if timestamp - self.timestamps[i] < 300:
                res += self.counter[i]
        return res


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
