class UndergroundSystem:

    def __init__(self):
        self.checkInRecords = dict()
        self.travelRecords = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInRecords[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkInStation, checkInTime = self.checkInRecords[id]
        path = (checkInStation, stationName)
        if path not in self.travelRecords:
            self.travelRecords[path] = []
        self.travelRecords[path].append(t-checkInTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        timeRecords = self.travelRecords[(startStation, endStation)]
        totalTime = 0
        for record in timeRecords:
            totalTime += record
        return totalTime/len(timeRecords)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)