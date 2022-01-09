class Solution:
    # BFS
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        buses = collections.defaultdict(set)
        for i in range(len(routes)):
            for stop in routes[i]:
                buses[stop].add(i)
        queue = [(source, 0)]
        visitedStop = set([source])
        visitedBus = set()
        while queue:
            currStop, numBus = queue.pop(0)
            if currStop == target:
                return numBus
            for bus in buses[currStop]:
                if bus not in visitedBus:
                    visitedBus.add(bus)
                    for stop in routes[bus]:
                        if stop not in visitedStop:
                            queue.append((stop, numBus+1))
                            visitedStop.add(stop)
        return -1