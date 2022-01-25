class TimeMap:

    def __init__(self):
        self.timeMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].insert(0, (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        value = self.timeMap.get(key)
        if not value:
            return ""
        for t, v in self.timeMap[key]:
            if t <= timestamp:
                return v
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)