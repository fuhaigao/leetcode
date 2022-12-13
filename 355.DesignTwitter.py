class Twitter:

    def __init__(self):
        self.counter = 0
        self.users = collections.defaultdict(User)

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = Tweet(tweetId, self.counter)
        self.counter += 1
        
        self.createUserIfNotExist(userId)
        self.users[userId].tweets.appendleft(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        maxHeap = []
        if len(self.users[userId].tweets) > 0:
            userTweet = self.users[userId].tweets[0]
            heapq.heappush(maxHeap, (-userTweet.count, userId, userTweet.id, 0))
        
        for follow in self.users[userId].follows:
            if len(follow.tweets) > 0:
                followTweet = follow.tweets[0]
                heapq.heappush(maxHeap, (-followTweet.count, follow.id, followTweet.id, 0))
        
        recentFeeds = []
        for i in range(10):
            if len(maxHeap) == 0:
                return recentFeeds
            tweetCount, userId, tweet, index = heapq.heappop(maxHeap)
            recentFeeds.append(tweet)
            index += 1
            if index < len(self.users[userId].tweets):
                nextTweet = self.users[userId].tweets[index]
                heapq.heappush(maxHeap, (-nextTweet.count, userId, nextTweet.id, index))
        return recentFeeds

    def follow(self, followerId: int, followeeId: int) -> None:
        self.createUserIfNotExist(followerId)
        self.createUserIfNotExist(followeeId)
        self.users[followerId].follows.add(self.users[followeeId])
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.createUserIfNotExist(followerId)
        self.createUserIfNotExist(followeeId)
        self.users[followerId].follows.discard(self.users[followeeId])
    
    def createUserIfNotExist(self, userId):
        if userId not in self.users:
            self.users[userId] = User(userId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

class User:
    
    def __init__(self, userId):
        self.id = userId
        self.follows = set()
        self.tweets = collections.deque()
        
class Tweet:
    
    def __init__(self, tweetId, tweetCount):
        self.id = tweetId
        self.count = tweetCount