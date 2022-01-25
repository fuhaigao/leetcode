class Solution:
    '''
    Greedy with priority queue 
    fact: the max distance does not depends on the position of stops, only the amount of fuel at each stop
    e.g. startFuel = 20, stations = [[10,60],[20,30],[30,30],[60,40]]
    distance we can reach:
    1. stop at station 0: 30 - 10 + 10 + 60 = 30+60
    2. stop at station 1: 30 - 20 + 20 + 30 = 30+30
    
    Therefore, for reachable stops at each round, we just stop at the one with maximum fuel
    
    Tricky Part: when current max distance < next stop, it does not mean that it is unreachable. We can simply add next fuel in pq, and increment count. This means that we must have an extra stop before current maximum to have more fuel for next move.
    '''
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        distance = startFuel
        index = 0
        count = 0
        pq = []
        while distance < target:
            while index < len(stations) and stations[index][0] <= distance:
                station = stations[index]
                heapq.heappush(pq, -station[1])
                index += 1
            if len(pq) == 0:
                return -1
            maxDistance = heapq.heappop(pq)
            distance -= maxDistance #use minus since negative value is pushed to min heap
            count += 1
        return count
            
        