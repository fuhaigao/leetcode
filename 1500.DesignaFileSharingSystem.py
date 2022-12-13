class FileSharing:

    def __init__(self, m: int):
        self.userIds = [1]
        self.chunksToUsers = collections.defaultdict(set)
        self.usersToChunks = collections.defaultdict(set)

    def join(self, ownedChunks: List[int]) -> int:
        userId = heapq.heappop(self.userIds)
        if not self.userIds:
            heapq.heappush(self.userIds, userId+1)
        self.usersToChunks[userId] = set(ownedChunks)
        for chunk in ownedChunks:
            self.chunksToUsers[chunk].add(userId)
        return userId

    def leave(self, userID: int) -> None:
        heapq.heappush(self.userIds, userID)
        for chunk in self.usersToChunks[userID]:
            self.chunksToUsers[chunk].remove(userID)
        self.usersToChunks[userID] = set()

    def request(self, userID: int, chunkID: int) -> List[int]:
        users = list(self.chunksToUsers[chunkID])
        users.sort()
        if len(users) > 0:
            self.usersToChunks[userID].add(chunkID)
            self.chunksToUsers[chunkID].add(userID)
        return users


# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)
